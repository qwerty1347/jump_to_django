from django.db import models

from common.models.base import Base
from common.models.timestamped import TimeStamped


class Question(Base, TimeStamped):
    subject = models.CharField(max_length=200)
    content = models.TextField()


    def __str__(self):
        return self.subject