from django.http import HttpRequest

from apps.pybo.question.models.question import Question
from apps.pybo.question.repositories.repository import QuestionRepository
from common.utils.pagination import get_paginated_queryset


class QuestionService:
    def __init__(self):
        self.repository = QuestionRepository()


    def get_paginated_questions(self, request: HttpRequest):
        questions = self.repository.get_questions()
        return get_paginated_queryset(list=questions, page=int(request.GET.get('page', 1)))


    def get_question(self, question_id: int) -> Question:
        return self.repository.get_question(question_id)


    def create_question(self, form_data: dict) -> Question:
        return self.repository.create_question(form_data)