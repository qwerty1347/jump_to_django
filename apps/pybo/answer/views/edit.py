from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from apps.pybo.answer.forms.create import AnswerCreateForm
from apps.pybo.answer.services.service import AnswerService
from apps.pybo.question.services.service import QuestionService
from common.constants.template import TemplateConstants
from common.utils.exception import handle_exception


answer_service = AnswerService()
question_service = QuestionService()


@require_http_methods(["POST"])
def update_answer(request: HttpRequest, answer_id: int):
    form = AnswerCreateForm(request.POST)

    try:
        answer = answer_service.update_answer(request, form, answer_id)
        messages.success(request, "답변이 수정되었습니다.")
        return redirect('pybo:question:detail', question_id=answer.question.pk)

    except Http404:
        raise Http404

    except ValueError:
        return render(request, TemplateConstants.PYBO['question']['detail'], {'form': form, 'question': answer.question})

    except PermissionDenied:
        messages.error(request, "권한이 없는 게시물입니다.")
        return redirect('pybo:question:detail', question_id=answer.question.pk)

    except Exception as e:
        handle_exception(e)
        messages.error(request, '답변 수정 오류')
        return render(request, TemplateConstants.PYBO['question']['detail'], {'form': form, 'question': answer.question})