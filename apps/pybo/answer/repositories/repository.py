from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone

from apps.pybo.answer.forms.create import AnswerCreateForm
from apps.pybo.answer.models.answer import Answer
from apps.pybo.question.models.question import Question


class AnswerRepository:
    def __init__(self):
        pass


    def get_answer(self, answer_id: int) -> Answer:
        return get_object_or_404(Answer, pk=answer_id)


    def create_answer(self, question: Question, form: AnswerCreateForm, user: User) -> Answer:
        answer = form.save(commit=False)
        answer.question = question
        answer.author = user
        answer.save()
        return answer


    def update_answer(self, answer_id: int, form_data: dict) -> Answer:
        answer = Answer.objects.get(pk=answer_id)

        for field, value in form_data.items():
            setattr(answer, field, value)

        answer.save()
        return answer


    def delete_answer(self, answer_id: int) -> int:
        return Answer.objects.filter(pk=answer_id).update(is_active=False, deleted_at=timezone.now())