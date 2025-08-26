from apps.pybo.answer.models.answer import Answer
from apps.pybo.question.models.question import Question


class AnswerRepository:
    def __init__(self):
        pass


    def create_answer(self, question: Question, data: dict) -> Answer:
        return question.answer_set.create(
            content=data['content'],
        )