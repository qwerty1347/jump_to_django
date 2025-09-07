from apps.pybo.answer.forms.create import AnswerCreateForm
from apps.pybo.answer.models.answer import Answer
from apps.pybo.answer.repositories.repository import AnswerRepository
from apps.pybo.question.repositories.repository import QuestionRepository


class AnswerService:
    def __init__(self):
        self.repository = AnswerRepository()
        self.question_repository = QuestionRepository()


    def create_answer(self, question_id: int, form: AnswerCreateForm) -> Answer:
        question = self.question_repository.get_question(question_id)
        return self.repository.create_answer(question, form)