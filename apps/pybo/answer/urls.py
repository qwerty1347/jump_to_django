from django.urls import path

from .views import create
from .views import edit
from .views import delete


app_name = "answer"

urlpatterns = [
    path('create/<int:question_id>/', create.create_answer, name="create"),
    path('edit/<int:answer_id>', edit.update_answer, name="edit"),
    path('delete/<int:answer_id>', delete.delete_answer, name="delete"),
]
