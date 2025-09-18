from http import HTTPStatus

from django.http import JsonResponse

from common.constants.http_code import HttpCodeConstants


def success_response(data: dict = None, code: int = HTTPStatus.OK.value) -> JsonResponse:
    if data is None:
        data = {}

    return JsonResponse(
        {
            "result": True,
            "code": code,
            "data": data
        },
        status=code
    )


def error_response(code: int = HttpCodeConstants.UNKNOWN_ERROR, message: str = "Internal Server Error") -> JsonResponse:
    return JsonResponse(
        {
            "result": False,
            "code": code,
            "message": message
        },
        status=code
    )