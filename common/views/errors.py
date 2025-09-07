from http import HTTPStatus
from django.http import HttpResponse
from django.shortcuts import render

from common.constants.template import TemplateConstants


def custom_404_error(request, exception) -> HttpResponse:
    context = {'message': str(exception) if exception else "페이지를 찾을 수 없습니다."}
    return render(request, TemplateConstants.ERRORS['404'], context, status=HTTPStatus.NOT_FOUND.value)


def custom_500_error(request) -> HttpResponse:
    return render(request, TemplateConstants.ERRORS['500'], status=HTTPStatus.INTERNAL_SERVER_ERROR.value)