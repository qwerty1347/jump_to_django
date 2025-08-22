from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index),
    path('question/', include('apps.pybo.question.urls'))
]
