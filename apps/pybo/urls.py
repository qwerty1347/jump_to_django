from django.urls import include, path
from . import views


app_name= "pybo"

urlpatterns = [
    path('', views.index),
    path('question/', include('apps.pybo.question.urls', namespace="question"))
]