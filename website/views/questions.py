from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from website.forms import QuestionForm


def question_form(request):
    """Отображение формы для вопроса посетителя"""

    q_form = QuestionForm(data=request.POST)

    if q_form.is_valid():
        q_form.save()

        send_mail(
            subject='На сайте питомника появился новый вопрос!',
            message='https://romashka-rat.ru/admin/website/question/',
            from_email='admin@romashka-rat.ru',
            recipient_list=['splendidcat@yandex.ru', 'romashka-rat@yandex.ru'],
        )

    return HttpResponseRedirect('../')
