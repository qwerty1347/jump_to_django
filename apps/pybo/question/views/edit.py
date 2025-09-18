from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from apps.pybo.question.forms.create import QuestionCreateForm
from apps.pybo.question.services.service import QuestionService
from common.constants.template import TemplateConstants
from common.utils.exception import handle_exception


question_service = QuestionService()


@require_http_methods(["GET", "POST"])
def modify_question(request: HttpRequest, question_id: int):
    try:
        if request.method == "GET":
            question = question_service.get_question(question_id)
            form = QuestionCreateForm(instance=question)

            return render(request, TemplateConstants.PYBO['question']['create'], {"form": form})

        elif request.method == "POST":
            question = question_service.update_question(request, question_id)
            messages.success(request, "질문이 수정되었습니다.")
            return redirect('pybo:question:detail', question_id=question.id)

    except Http404:
        raise Http404

    except ValueError:
        form = QuestionCreateForm(request.POST)
        return render(request, TemplateConstants.PYBO['question']['create'], {'form': form})

    except PermissionDenied:
        messages.error(request, "권한이 없는 게시물입니다.")
        return redirect('pybo:question:edit', question_id=question_id)

    except Exception as e:
        handle_exception(e)
        messages.error(request, "질문 수정 오류 발생")