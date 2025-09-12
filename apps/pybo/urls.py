from django.contrib.auth import views as auth_views
from django.urls import include, path

from apps.common.auth.views import auth
from common.constants.template import TemplateConstants


app_name= "pybo"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name=TemplateConstants.PYBO['user']['login']), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', auth.signup, name="signup"),
    path('question/', include('apps.pybo.question.urls', namespace="question")),
    path('answer/', include('apps.pybo.answer.urls', namespace="answer")),
]