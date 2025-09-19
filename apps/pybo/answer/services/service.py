from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest

from apps.pybo.answer.forms.create import AnswerCreateForm
from apps.pybo.answer.models.answer import Answer
from apps.pybo.answer.repositories.repository import AnswerRepository
from apps.pybo.question.repositories.repository import QuestionRepository


class AnswerService:
    def __init__(self):
        self.answer_repository = AnswerRepository()
        self.question_repository = QuestionRepository()


    def get_answer(self, answer_id: int) -> Answer:
        return self.answer_repository.get_answer(answer_id)


    def create_answer(self, request: HttpRequest, form: AnswerCreateForm, question_id: int) -> Answer:
        if form.is_valid():
            question = self.question_repository.get_question(question_id)

            form_data = form.cleaned_data
            form_data['author'] = request.user

            return self.answer_repository.create_answer(question, form, request.user)

        else:
            raise ValueError


    def update_answer(self, request: HttpRequest, form: AnswerCreateForm, answer_id: int) -> Answer:
        if form.is_valid():
            answer = self.answer_repository.get_answer(answer_id)

            if request.user != answer.author:
                raise PermissionDenied()

            else:
                form_data = form.cleaned_data
                return self.answer_repository.update_answer(answer.id, form_data)

        else:
            raise ValueError


    def delete_answer(self, request, answer_id):
        answer = self.answer_repository.get_answer(answer_id)

        if request.user != answer.author:
            raise PermissionDenied()

        else:
            return self.answer_repository.delete_answer(answer_id)