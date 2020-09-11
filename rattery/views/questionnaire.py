from django.shortcuts import render, redirect

from rattery.forms import QuestionnaireForm


def questionnaire_form(request):
    if request.method != 'POST':
        form = QuestionnaireForm()
    else:
        form = QuestionnaireForm(data=request.POST)
        form.save()
        return redirect(questionnaire_success)
    context = {'form': form}
    return render(request, 'rattery/questionnaire.html', context)


def questionnaire_success(request):
    return render(request, 'rattery/success.html')
