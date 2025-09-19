from http import HTTPStatus

from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpRequest, HttpResponse
from django.views.decorators.http import require_http_methods

from apps.pybo.answer.services.service import AnswerService
from common.utils.exception import handle_exception
from common.utils.response import error_response, success_response


answer_service = AnswerService()


@require_http_methods(["DELETE"])
def delete_answer(request: HttpRequest, answer_id: int) -> HttpResponse:
    try:
        affected_rows = answer_service.delete_answer(request, answer_id)
        return success_response({"affected_rows": affected_rows})

    except Http404:
        return error_response(HTTPStatus.NOT_FOUND.value, "존재하지 않는 답변입니다.")

    except PermissionDenied:
        print(222)
        return error_response(HTTPStatus.FORBIDDEN.value, "권한이 없는 답변입니다.")

    except Exception as e:
        print(12345)
        handle_exception(e)
        return error_response(message=str(e))