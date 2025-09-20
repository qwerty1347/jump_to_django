from django.contrib.auth.models import User
from django.db import models

from common.models.base import Base
from common.models.timestamped import TimeStamped


class Question(Base, TimeStamped):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="question_author")
    voter = models.ManyToManyField(User, related_name="question_voters")


    def __str__(self):
        return self.subject