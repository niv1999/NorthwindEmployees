from logic.auth_logic import AuthLogic
from flask import request, session
from models.role_model import RoleModel
from models.user_model import UserModel
from models.client_errors import ValidationError, AuthError
from models.credentials_model import CredentialsModel

class AuthFacade:

    def __init__(self):
        self.logic = AuthLogic()

    def register(self):
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        user = UserModel(None, first_name, last_name, email, password, RoleModel.User.value)
        error = user.validate_insert()
        if error: raise ValidationError(error, user)
        if self.logic.is_email_taken(email): raise ValidationError("Email already exists.", user)
        self.logic.add_user(user)

    def login(self):
        email = request.form.get("email")
        password = request.form.get("password")
        credentials = CredentialsModel(email, password)
        error = credentials.validate()
        if error: raise ValidationError(error, credentials)
        user = self.logic.get_user(credentials)
        if not user: raise AuthError("Incorrect email or password.", credentials)
        session["current_user"] = user

    def logout(self):
        session.clear()

    def block_anonymous(self):
        user = session.get("current_user")
        if not user: raise AuthError("You are not logged in.")
    
    def block_non_admin(self):
        user = session.get("current_user")
        if not user: raise AuthError("You are not logged in.")
        if user["role_id"] != RoleModel.Admin.value: raise AuthError("You are not allowed.")

    def close(self):
        self.logic.close()
        
