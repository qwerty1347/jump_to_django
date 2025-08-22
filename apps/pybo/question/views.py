from django.conf import settings
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
import environ

from apps.pybo.question.services.service import QuestionService


question_service = QuestionService()


def index(request):
    try:
        result = question_service.get_questions()
        # return HttpResponse(result)

        # raise Http404("해당 질문을 찾을 수 없습니다.")

        

        print(settings.DEBUG, '=============@')

        return HttpResponse("Hello, Pybo Question!")

        # raise Exception("테스트용 500 에러")

        

    except Exception as e:
        raise e
    