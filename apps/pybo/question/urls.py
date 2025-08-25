from django.urls import path

from .views import list
from .views import detail


app_name = "question"

urlpatterns = [
    path('', list.question_list, name="list"),
    path('<int:question_id>/', detail.question_detail, name="detail")
]