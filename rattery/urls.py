from django.urls import path
from rattery.views import rats, questionnaire

urlpatterns = [
    # крысы
    path('available/', rats.available, name='available'),
    path('male/', rats.male_rats, name='male_rats'),
    path('female/', rats.female_rats, name='female_rats'),
    path('<int:rat_id>/', rats.rat, name='rat'),
    # пометы
    path('litters/<int:litter_year>/', rats.litters, name='litters'),
    path('litters/<int:litter_year>/<int:litter_id>/', rats.litter, name='litter'),
    path('litters/<int:litter_year>/<int:litter_id>/csv', rats.csv_pedigree, name='csv_pedigree'),
    # анкета
    path('questionnaire/', questionnaire.questionnaire_form, name='questionnaire_form'),
    path('questionnaire/success/', questionnaire.questionnaire_success, name='questionnaire_success'),
]
