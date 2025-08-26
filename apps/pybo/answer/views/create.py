from django.contrib import messages
from django.http import Http404, HttpResponse
from django.shortcuts import redirect

from apps.pybo.answer.forms.create import AnswerCreateForm
from apps.pybo.answer.services.service import AnswerService
from common.utils.exception import handle_exception


answer_service = AnswerService()


def create_answer(request, question_id: int):
    # TODO: POST 외 405 처리

    form = AnswerCreateForm(request.POST)

    if not form.is_valid():
        return HttpResponse("hello, form", status=422)

    try:
        answer =  answer_service.create_answer(question_id, form.cleaned_data)

        if answer:
            messages.success(request, "답변 등록완료")
            return redirect('pybo:question:detail', question_id)

    except Http404:
        raise

    except Exception as e:
        handle_exception(e)