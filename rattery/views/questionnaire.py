from django.shortcuts import render, redirect
from rattery.forms import QuestionnaireForm


def questionnaire_form(request):
    """Форма для заполнения анкеты"""
    if request.method != 'POST':
        form = QuestionnaireForm()
    else:
        form = QuestionnaireForm(data=request.POST)
        form.save()
        return redirect(questionnaire_success)
    context = {'form': form}
    return render(request, 'rattery/questionnaire.html', context)


def questionnaire_success(request):
    """Отображение страницы успешного заполнения анкеты"""
    return render(request, 'rattery/questionnaire_success.html')
