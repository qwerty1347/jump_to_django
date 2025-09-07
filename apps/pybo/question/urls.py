from django.urls import path

from .views import list
from .views import detail
from .views import create


app_name = "question"

urlpatterns = [
    path('', list.question_list, name="list"),
    path('<int:question_id>/', detail.question_detail, name="detail"),
    path('create/', create.create_question, name="create"),
]