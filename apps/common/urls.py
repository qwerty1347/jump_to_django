from django.urls import include, path


app_name = "common"

urlpatterns = [
    path('', include('apps.common.auth.urls', namespace="auth")),
]
