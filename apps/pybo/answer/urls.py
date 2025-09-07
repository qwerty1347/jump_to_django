from django.urls import path

from .views import create


app_name = "answer"

urlpatterns = [
    path('create/<int:question_id>/', create.create_answer, name="create")
]
