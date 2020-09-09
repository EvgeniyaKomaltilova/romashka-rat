from django.shortcuts import render

from website.forms import QuestionnaireForm
from django.shortcuts import render, redirect


def questionnaire_form(request):
    if request.method != 'POST':
        form = QuestionnaireForm()
    else:
        form = QuestionnaireForm(data=request.POST)
        form.save()
        return redirect(questionnaire_success)
    context = {'form': form}
    return render(request, 'website/questionnaire.html', context)


def questionnaire_success(request):
    return render(request, 'website/success.html')
