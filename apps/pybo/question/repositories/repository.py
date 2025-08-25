from apps.pybo.question.models.question import Question


class QuestionRepository:
    def __init__(self):
        pass
    
    
    def get_questions(self):
        return Question.objects.order_by('-created_at')