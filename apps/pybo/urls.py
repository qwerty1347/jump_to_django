from django.contrib.auth import views as auth_views
from django.urls import include, path
from . import views


app_name= "pybo"

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='pybo/common/login.html'), name="login"),
    path('question/', include('apps.pybo.question.urls', namespace="question")),
    path('answer/', include('apps.pybo.answer.urls', namespace="answer")),
]