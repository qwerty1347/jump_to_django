from django.db.models.query import QuerySet

from apps.pybo.question.models.question import Question
from apps.pybo.question.repositories.repository import QuestionRepository


class QuestionService:
    def __init__(self):
        self.repository = QuestionRepository()


    def get_questions(self) -> QuerySet[Question]:
        return self.repository.get_questions


    def get_question(self, question_id: int) -> Question:
        return self.repository.get_question(question_id)


    def create_question(self, form_data: dict) -> Question:
        return self.repository.create_question(form_data)