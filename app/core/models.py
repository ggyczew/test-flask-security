from app import db
# from flask import current_app as app
from flask_security.models import fsqla_v3 as fsqla
from flask_security import AsaList

# Define models - for this example - we change the default table names
fsqla.FsModels.set_db_info(db, user_table_name="users", role_table_name="roles")

class Role(db.Model, fsqla.FsRoleMixin):
    __tablename__ = "roles"
    permissions = db.Column(AsaList())


class User(db.Model, fsqla.FsUserMixin):
    __tablename__ = "users"

