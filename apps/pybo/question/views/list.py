from http import HTTPStatus
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.pybo.question.services.service import QuestionService
from common.constants.template import TemplateConstants
from common.utils.exception import handle_exception


question_service = QuestionService()


def question_list(request: HttpRequest) -> HttpResponse:
    try:
        context = question_service.get_paginated_questions(request)
        return render(request, TemplateConstants.PYBO['question']['list'], context)

    except Exception as e:
        handle_exception(e)
        return render(request, TemplateConstants.ERRORS['500'], status=HTTPStatus.INTERNAL_SERVER_ERROR.value)