from django.urls import path

from .views import create


app_name = "answer"

urlpatterns = [
    path('', create.create_answer, name="create")
]
