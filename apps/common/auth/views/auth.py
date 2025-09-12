from django.http import HttpRequest, HttpResponse


def signup(request: HttpRequest):
    return HttpResponse("signup")