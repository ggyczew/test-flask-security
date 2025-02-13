import os
from dotenv import load_dotenv
import logging

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Config(object):

    DEBUG = os.environ.get("DEBUG")

    ADMINS = frozenset(["admin@me.com"])
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-key"
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

    CSRF_ENABLED = True
    CSRF_SESSION_KEY = os.environ.get("CSRF_SESSION_KEY")

    REMEMBER_COOKIE_SAMESITE = "strict"
    SESSION_COOKIE_SAMESITE = "strict"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_pre_ping": True}
    SQLALCHEMY_RECORD_QUERIES = True

    SECURITY_TRACKABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_PASSWORD_HASH = "argon2"
    SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT")
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_POST_LOGOUT_VIEW = "/loggedout"


class DevelopmentConfig(Config):
    DEBUG = True
    LOGGING_LEVEL = logging.DEBUG
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.sqlite")
    SQLALCHEMY_BINDS = {}


config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig,
}
