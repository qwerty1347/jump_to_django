from apps.pybo.question.repositories.repository import QuestionRepository


class QuestionService:
    def __init__(self):
        self.repository = QuestionRepository()
        
        
    def get_questions(self):
        pass
