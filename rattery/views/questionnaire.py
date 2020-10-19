from django.core.mail import send_mail
from django.shortcuts import render, redirect
from rattery.forms import QuestionnaireForm
from romashka import settings


def questionnaire_form(request):
    """Форма для заполнения анкеты"""

    if request.method != 'POST':
        form = QuestionnaireForm()
    else:
        form = QuestionnaireForm(data=request.POST)
        form.save()

        send_mail(
            subject='На сайте питомника появилась новая анкета!',
            message='https://romashka-rat.ru/admin/rattery/questionnaire/',
            from_email='admin@romashka-rat.ru',
            recipient_list=['splendidcat@yandex.ru', 'romashka-rat@yandex.ru'],
        )

        return redirect(questionnaire_success)

    context = {'form': form}
    return render(request, 'rattery/questionnaire.html', context)


def questionnaire_success(request):
    """Отображение страницы успешного заполнения анкеты"""
    return render(request, 'rattery/questionnaire_success.html')
