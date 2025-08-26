from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from apps.pybo.answer.forms.create import AnswerCreateForm
from apps.pybo.answer.services.service import AnswerService
from apps.pybo.question.repositories.repository import QuestionRepository
from common.constants.template import TemplateConstants
from common.utils.exception import handle_exception


answer_service = AnswerService()


def create_answer(request, question_id: int):
    # TODO: POST 외 405 처리

    form = AnswerCreateForm(request.POST)
    question_repository = QuestionRepository()

    if not form.is_valid():
        context = {'form': form, 'question': question_repository.get_question(question_id)}
        return render(request, TemplateConstants.PYBO['question']['detail'], context)

    try:
        answer =  answer_service.create_answer(question_id, form.cleaned_data)

        if answer:
            messages.success(request, "답변 등록완료")
            return redirect('pybo:question:detail', question_id=question_id)

    except Http404:
        raise

    except Exception as e:
        handle_exception(e)