from django.contrib import messages
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from apps.pybo.answer.forms.create import AnswerCreateForm
from apps.pybo.answer.services.service import AnswerService
from apps.pybo.question.services.service import QuestionService
from common.constants.template import TemplateConstants
from common.utils.exception import handle_exception


question_service = QuestionService()
answer_service = AnswerService()


@require_POST
def create_answer(request: HttpRequest, question_id: int) -> HttpResponse:
    question = question_service.get_question(question_id)
    form = AnswerCreateForm(request.POST)

    if form.is_valid():
        try:
            answer_service.create_answer(question_id, form, request.user)
            messages.success(request, "답변 등록 완료")
            return redirect('pybo:question:detail', question_id=question_id)

        except Http404:
            raise

        except Exception as e:
            handle_exception(e)
            messages.error(request, "답변 생성 오류")

    else:
        context = {'form': form, 'question': question}
        return render(request, TemplateConstants.PYBO['question']['detail'], context)