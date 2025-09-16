from django.contrib.auth.models import User

from apps.common.auth.repositories.repository import AuthRepository


class AuthService:
    def __init__(self):
        self.auth_repository = AuthRepository()


    def create_user(self, form_data) -> User:
        self.auth_repository.create_user(form_data)