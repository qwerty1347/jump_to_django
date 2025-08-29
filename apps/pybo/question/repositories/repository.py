from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

from apps.pybo.question.models.question import Question


class QuestionRepository:
    def __init__(self):
        pass


    def get_questions(self) -> QuerySet[Question]:
        return Question.objects.order_by('-created_at')


    def get_question(self, question_id: int) -> Question:
        return get_object_or_404(Question, pk=question_id)


    def create_question(self, form_data: dict) -> Question:
        return Question.objects.create(**form_data)