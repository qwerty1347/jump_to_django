from django.contrib.auth.models import User

from apps.pybo.answer.forms.create import AnswerCreateForm
from apps.pybo.answer.models.answer import Answer
from apps.pybo.question.models.question import Question


class AnswerRepository:
    def __init__(self):
        pass


    def create_answer(self, question: Question, form: AnswerCreateForm, user: User) -> Answer:
        answer = form.save(commit=False)
        answer.question = question
        answer.author = user
        answer.save()
        return answer