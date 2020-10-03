from django import forms

from website.models.Question import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question

        fields = ['email', 'text']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'inp', 'placeholder': 'Введите e-mail для связи'}),
            'text': forms.Textarea(attrs={'placeholder': 'Введите ваш вопрос'}),
        }
