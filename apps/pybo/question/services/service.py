from django.contrib.auth.models import User
from django.http import HttpRequest

from apps.pybo.question.models.question import Question
from apps.pybo.question.repositories.repository import QuestionRepository
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