from django.http import HttpResponse
from django.shortcuts import render

from apps.pybo.question.services.service import QuestionService


question_service = QuestionService()


def index(request):
    try:
        return HttpResponse("Hello, Pybo Question!")


        result = question_service.get_questions()
        return HttpResponse(f"<pre>{pformat(result)}</pre>")



    except Exception as e:
        print(f"ERROR: {str(e)}")
        return render(request, "errors/500.html", status=500)