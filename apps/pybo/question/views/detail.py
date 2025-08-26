import traceback

from http import HTTPStatus
from django.http import Http404, HttpResponse
from django.shortcuts import render

from apps.pybo.question.services.service import QuestionService
from common.constants.template import TemplateConstants


question_service = QuestionService()


def question_detail(request, question_id: int) -> HttpResponse:
    try:
        question = question_service.get_question(question_id)
        context = {'question': question}
        return render(request, TemplateConstants.PYBO['question']['detail'], context)

    except Http404:
        raise

    except Exception as e:
        print(f"ERROR: {str(e)}")
        traceback.print_exc()
        return render(request, TemplateConstants.ERRORS['500'], status=HTTPStatus.INTERNAL_SERVER_ERROR.value)