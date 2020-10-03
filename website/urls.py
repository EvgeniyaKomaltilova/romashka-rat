from django.urls import path
from website.views import entries, questions

app_name = 'website'

urlpatterns = [
    path('', entries.main_page, name='index'),
    path('about/', entries.about, name='about'),
    path('archive/', entries.archive, name='archive'),
    path('contract/', entries.contract, name='contract'),
    path('varieties/', entries.varieties, name='varieties'),
    path('colors/', entries.colors, name='colors'),
    path('markings/', entries.markings, name='markings'),
    path('question/', questions.question_form, name='question')
]
