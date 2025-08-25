from http import HTTPStatus
from django.http import HttpResponse
from django.shortcuts import render

from common.constants.template import TemplateConstants


def custom_500_error(request) -> HttpResponse:
    return render(request, TemplateConstants.ERRORS['500'], status=HTTPStatus.INTERNAL_SERVER_ERROR.value)