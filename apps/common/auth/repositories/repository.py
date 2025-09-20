from django.contrib.auth.models import User


class AuthRepository:
    def __init__(self):
        pass


    def create_user(self, form_data: dict) -> User:
        return User.objects.create_user(**form_data)