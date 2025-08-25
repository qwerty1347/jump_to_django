from django.shortcuts import render

from apps.pybo.question.services.service import QuestionService
from common.constants.template import TemplateConstants


question_service = QuestionService()


def index(request):
    try:
        questions = question_service.get_questions()
        context = {'questions': questions}
        return render(request, TemplateConstants.TEMPLATES['pybo']['question']['index'], context)
        
    except Exception as e:
        raise e