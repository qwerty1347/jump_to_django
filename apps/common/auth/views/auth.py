from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from apps.common.auth.forms.user_create import UserCreateForm
from common.constants.template import TemplateConstants


@require_http_methods(["GET", "POST"])
def signup(request: HttpRequest):
    if request.method == "GET":
        form = UserCreateForm()
        return render(request, TemplateConstants.PYBO['user']['signup'], {'form': form})

    elif request.method == "POST":
        form = UserCreateForm(request.POST)

        if form.is_valid():
            try:
                pass

            except Exception as e:
                raise e

        else:
            return render(request, TemplateConstants.PYBO['user']['signup'], {'form': form})