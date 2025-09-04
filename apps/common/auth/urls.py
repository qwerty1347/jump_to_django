from django.urls import path
from .views import auth


app_name = "auth"

urlpatterns = [
    path('login/', auth.login, name="login"),
]
