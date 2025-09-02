from django import forms

from apps.pybo.answer.models.answer import Answer


class AnswerCreateForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }