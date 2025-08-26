from django import forms


class AnswerCreateForm(forms.Form):
    content = forms.CharField(max_length=200, required=True)