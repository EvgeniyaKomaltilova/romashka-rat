from django import forms
from rattery.models.Questionnaire import Questionnaire


class QuestionnaireForm(forms.ModelForm):
    """Форма анкеты для потенциального владельца"""

    class Meta:
        model = Questionnaire

        fields = ['name', 'contact', 'age', 'location', 'which_baby_rat', 'allergy', 'know_how', 'pet_or_breed',
                  'friend', 'contract', 'recommendation', 'additionally']

        labels = {
            'name': 'Ваше имя',
            'contact': 'Страница вКонтакте или e-mail для связи',
            'age': 'Сколько вам полных лет?',
            'location': 'Где вы проживаете?',
            'which_baby_rat': 'Какой крысенок (крысята) вас интересует?',
            'allergy': 'Есть ли у вас или кого-то из вашей семьи астма или аллергия на животных? '
                       'Это самая частая причина, по которой люди возвращают крыс назад.',
            'know_how': 'Содержали ли вы крыс до этого? Если вы новичок, то изучили ли всю необходимую информацию '
                     'о содержании крыс?',
            'pet_or_breed': 'Вы хотите приобрести крысенка как домашнего любимца или под разведение?',
            'friend': 'Крысы - социальные животные. Будет ли у крысенка однополый друг, равный по возрасту?',
            'contract': 'Готовы ли Вы подписать договор* купли-продажи на животное?',
            'recommendation': 'Есть ли кто-то из крысоводов, кто мог бы Вас порекомендовать?',
            'additionally': 'Расскажите что-нибудь о себе',
        }

        widgets = {
            'allergy': forms.Textarea(attrs={'rows': 1, 'cols': 1, 'style': 'height: 5em; width:100%'}),
            'know_how': forms.Textarea(attrs={'rows': 1, 'cols': 1, 'style': 'height: 5em; width:100%'}),
            'pet_or_breed': forms.Textarea(attrs={'rows': 1, 'cols': 1, 'style': 'height: 5em; width:100%'}),
            'friend': forms.Textarea(attrs={'rows': 1, 'cols': 1, 'style': 'height: 5em; width:100%'}),
            'contract': forms.Textarea(attrs={'rows': 1, 'cols': 1, 'style': 'height: 5em; width:100%'}),
            'recommendation': forms.Textarea(attrs={'rows': 1, 'cols': 1, 'style': 'height: 5em; width:100%'}),
            'additionally': forms.Textarea(attrs={'rows': 1, 'cols': 1, 'style': 'height: 10em; width:100%'}),
        }
