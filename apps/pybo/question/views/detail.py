from http import HTTPStatus
from django.http import Http404
from django.shortcuts import render
from apps.pybo.question.models.question import Question
from apps.pybo.question.services.service import QuestionService
from common.constants.template import TemplateConstants


question_service = QuestionService()


def question_detail(request, question_id: int):
    try:
        question = question_service.get_question(question_id)
        context = {'question': question}
        return render(request, TemplateConstants.PYBO['question']['detail'], context)

    except Question.DoesNotExist:
        raise Http404("질문을 찾을 수 없습니다.")

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return render(request, TemplateConstants.ERRORS['500'], status=HTTPStatus.INTERNAL_SERVER_ERROR.value)