from django.db.models import Count
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django.utils import timezone

from apps.pybo.question.models.question import Question


class QuestionRepository:
    def __init__(self):
        pass


    def get_questions(self) -> QuerySet[Question]:
        return Question.objects.annotate(answer_count=Count('answers')).order_by('-created_at')


    def get_question(self, question_id: int) -> Question:
        return get_object_or_404(Question, pk=question_id)


    def create_question(self, form_data: dict) -> Question:
        return Question.objects.create(**form_data)


    def update_question(self, form_data: dict, question_id: int) -> Question:
        question = Question.objects.get(pk=question_id)

        for field, value in form_data.items():
            setattr(question, field, value)

        question.save()
        return question


    def delete_question(self, question_id: int) -> int:
        return Question.objects.filter(pk=question_id).update(is_active=False, deleted_at=timezone.now())