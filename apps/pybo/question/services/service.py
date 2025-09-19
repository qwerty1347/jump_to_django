from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest
from django.shortcuts import redirect, render

from apps.pybo.question.forms.create import QuestionCreateForm
from apps.pybo.question.models.question import Question
from apps.pybo.question.repositories.repository import QuestionRepository
from common.constants.template import TemplateConstants
from common.utils.pagination import get_paginated_queryset


class QuestionService:
    def __init__(self):
        self.question_repository = QuestionRepository()


    def get_paginated_questions(self, request: HttpRequest) -> dict:
        questions = self.question_repository.get_questions()
        return get_paginated_queryset(list=questions, page=int(request.GET.get('page', 1)))


    def get_question(self, question_id: int) -> Question:
        return self.question_repository.get_question(question_id)


    def create_question(self, form_data: dict, user: User) -> Question:
        form_data['author'] = user
        return self.question_repository.create_question(form_data)


    def update_question(self, request: HttpRequest, form: QuestionCreateForm, question_id: int):
        if form.is_valid():
            question = self.question_repository.get_question(question_id)

            if request.user != question.author:
                raise PermissionDenied()

            else:
                form_data = form.cleaned_data
                form_data['author'] = request.user

                return self.question_repository.update_question(question_id, form_data)

        else:
            raise ValueError


    def delete_question(self, request: HttpRequest, question_id: int):
        question = self.question_repository.get_question(question_id)

        if request.user != question.author:
            raise PermissionDenied()

        else:
            self.question_repository.delete_question(question_id)