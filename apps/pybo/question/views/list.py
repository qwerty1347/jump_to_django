from http import HTTPStatus
from django.shortcuts import render

from apps.pybo.question.services.service import QuestionService
from common.constants.template import TemplateConstants


question_service = QuestionService()


def question_list(request):
    try:
        questions = question_service.get_questions()
        context = {'questions': questions}
        return render(request, TemplateConstants.PYBO['question']['list'], context)
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return render(request, TemplateConstants.ERRORS['500'], status=HTTPStatus.INTERNAL_SERVER_ERROR.value)