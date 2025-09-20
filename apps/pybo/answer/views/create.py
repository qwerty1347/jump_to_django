from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from apps.pybo.answer.forms.create import AnswerCreateForm
from apps.pybo.answer.services.service import AnswerService
from apps.pybo.question.services.service import QuestionService
from common.constants.template import TemplateConstants
from common.utils.exception import handle_exception


question_service = QuestionService()
answer_service = AnswerService()


@login_required(login_url="pybo:login")
@require_http_methods(["GET", "POST"])
def create_answer(request: HttpRequest, question_id: int) -> HttpResponse:
    if request.method == "GET":
        return redirect('pybo:question:detail', question_id=question_id)

    elif request.method == "POST":
        form = AnswerCreateForm(request.POST)

        try:
            question = answer_service.create_answer(request, form, question_id)
            return redirect('pybo:question:detail', question_id=question_id)

        except ValueError:
            return render(request, TemplateConstants.PYBO['question']['detail'], {'form': form, 'question': question})

        except Http404:
            raise Http404

        except Exception as e:
            handle_exception(e)
            messages.error(request, '답변 생성 오류')
            return render(request, TemplateConstants.PYBO['question']['detail'], {'form': form, 'question': question})