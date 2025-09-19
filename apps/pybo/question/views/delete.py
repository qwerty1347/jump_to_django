from http import HTTPStatus

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpRequest, JsonResponse
from django.views.decorators.http import require_http_methods

from apps.pybo.question.services.service import QuestionService
from common.utils.exception import handle_exception
from common.utils.response import error_response, success_response


question_service = QuestionService()


@login_required(login_url='pybo:login')
@require_http_methods(["DELETE"])
def delete_question(request: HttpRequest, question_id: int) -> JsonResponse:
    try:
        affected_rows = question_service.delete_question(request, question_id)
        return success_response({"affected_rows": affected_rows})

    except Http404:
        return error_response(HTTPStatus.NOT_FOUND.value, "존재하지 않는 게시물입니다.")

    except PermissionDenied:
        return error_response(HTTPStatus.FORBIDDEN.value, "권한이 없는 게시물입니다.")

    except Exception as e:
        handle_exception(e)
        return error_response(message=str(e))