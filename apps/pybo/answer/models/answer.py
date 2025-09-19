from django.contrib.auth.models import User
from django.db import models

from apps.pybo.question.models.question import Question
from common.models.base import Base
from common.models.timestamped import TimeStamped


class Answer(Base, TimeStamped):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    voter = models.ManyToManyField(User, related_name="answer_voters")