from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from apps.common.auth.forms.user_create import UserCreateForm
from apps.common.auth.services.service import AuthService
from common.constants.template import TemplateConstants
from common.utils.exception import handle_exception


auth_service = AuthService()


@require_http_methods(["GET", "POST"])
def signup(request: HttpRequest):
    if request.method == "GET":
        form = UserCreateForm()
        return render(request, TemplateConstants.PYBO['user']['signup'], {'form': form})

    elif request.method == "POST":
        form = UserCreateForm(request.POST)

        if form.is_valid():
            try:
                form_data = form.cleaned_data
                auth_service.create_user({
                    "username": form_data['username'],
                    "password": form_data['password1'],
                    "email": form_data['email'],
                })

                messages.success(request, "사용자 생성 완료")
                return redirect('pybo:login')

            except Exception as e:
                handle_exception(e)
                messages.error(request, "사용자 생성 오류")
                raise e

        else:
            return render(request, TemplateConstants.PYBO['user']['signup'], {'form': form})