from django.contrib.auth.models import User

from apps.pybo.answer.forms.create import AnswerCreateForm
from apps.pybo.answer.models.answer import Answer
from apps.pybo.answer.repositories.repository import AnswerRepository
from apps.pybo.question.repositories.repository import QuestionRepository


class AnswerService:
    def __init__(self):
        self.answer_repository = AnswerRepository()
        self.question_repository = QuestionRepository()


    def create_answer(self, question_id: int, form: AnswerCreateForm, user: User) -> Answer:
        question = self.question_repository.get_question(question_id)
        return self.answer_repository.create_answer(question, form, user)