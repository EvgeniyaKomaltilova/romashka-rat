from django.shortcuts import render, redirect

from website.forms import QuestionForm


def question_form(request):
    """Форма для вопроса посетителя"""

    q_form = QuestionForm(data=request.POST)

    if q_form.is_valid():
        q_form.save()

    return redirect('../')
