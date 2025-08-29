from django import forms

from apps.pybo.question.models.question import Question


class QuestionCreateForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }