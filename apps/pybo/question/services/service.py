from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render

from apps.pybo.question.forms.create import QuestionCreateForm
from apps.pybo.question.models.question import Question
from apps.pybo.question.repositories.repository import QuestionRepository
from common.constants.template import TemplateConstants


class QuestionService:
    def __init__(self):
        self.repository = QuestionRepository()


    def get_questions(self) -> QuerySet[Question]:
        return self.repository.get_questions


    def get_question(self, question_id: int) -> Question:
        return self.repository.get_question(question_id)


    def get_create_from(self, request) -> HttpResponse:
        form = QuestionCreateForm()
        return render(request, TemplateConstants.PYBO['question']['create'], {'form': form})


    def create_question(self, form_data: dict) -> Question:
        return self.repository.create_question(form_data)