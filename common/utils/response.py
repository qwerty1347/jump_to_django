from http import HTTPStatus

from django.http import JsonResponse


def success_response(data: dict = None, code: int = HTTPStatus.OK.value) -> JsonResponse:
    """
    성공 응답을 반환하는 함수

    매개변수:
    - data (dict): 응답 데이터 (기본값: None)
    - code (int): 응답 코드 (기본값: 200)

    반환값:
    - JsonResponse: 응답을 JSON 형식으로 반환하는 HttpResponse
    """
    if data is None:
        data = {}

    return JsonResponse(
        data={
            "result": True,
            "code": code,
            "data": data
        },
        status=code
    )
    
    
def error_response(code: int = HTTPStatus.INTERNAL_SERVER_ERROR.value, message: str = "Internal Server Error") -> JsonResponse:
    """
    에러 응답을 반환하는 함수

    매개변수:
    - code (int): 응답 코드 (기본값: 500)
    - message (str): 에러 메시지 (기본값: "Internal Server Error")

    반환값:
    - JsonResponse: 응답을 JSON 형식으로 반환하는 HttpResponse
    """    
    return JsonResponse(
        data={
            "result": False,
            "code": code,
            "message": message
        },
        status=code
    )