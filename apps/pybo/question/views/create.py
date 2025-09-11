from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from apps.pybo.question.forms.create import QuestionCreateForm
from apps.pybo.question.services.service import QuestionService
from common.constants.template import TemplateConstants
from common.utils.exception import handle_exception


question_service = QuestionService()


@require_http_methods(["GET", "POST"])
def create_question(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = QuestionCreateForm()
        return render(request, TemplateConstants.PYBO['question']['create'], {'form': form})

    elif request.method == "POST":
        form = QuestionCreateForm(request.POST)

        if form.is_valid():
            try:
                question = question_service.create_question(form.cleaned_data)
                messages.success(request, "질문 등록 완료")
                return redirect('pybo:question:detail', question_id=question.id)

            except Exception as e:
                handle_exception(e)
                messages.error(request, "질문 생성 오류")

        else:
            return render(request, TemplateConstants.PYBO['question']['create'], {'form': form})