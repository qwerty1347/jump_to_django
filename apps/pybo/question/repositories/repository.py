from django.db.models.query import QuerySet

from apps.pybo.question.models.question import Question


class QuestionRepository:
    def __init__(self):
        pass


    def get_questions(self) -> QuerySet[Question]:
        return Question.objects.order_by('-created_at')


    def get_question(self, question_id: int) -> Question:
        return Question.objects.get(id=question_id)