from http import HTTPStatus
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from apps.pybo.question.forms.create import QuestionCreateForm
from apps.pybo.question.services.service import QuestionService
from common.constants.template import TemplateConstants
from common.utils.exception import handle_exception


question_service = QuestionService()

@require_http_methods(["GET", "POST"])
def create_question(request) -> HttpResponse:

    if request.method == "GET":
        return question_service.get_create_from(request)

    elif request.method == "POST":
        form = QuestionCreateForm(request.POST)

        if not form.is_valid():
            return render(request, TemplateConstants.PYBO['question'], {'form': form})

        try:
            question = question_service.create_question(form.cleaned_data)
            print(question)

        except Exception as e:
            handle_exception(e)
            return render(request, TemplateConstants.ERRORS['500'], status=HTTPStatus.INTERNAL_SERVER_ERROR.value)


    return HttpResponse("Hello, Django Pybo!")
