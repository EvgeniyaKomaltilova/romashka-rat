from django import template
from website.forms import QuestionForm

register = template.Library()


@register.simple_tag()
def question_form():
    return QuestionForm()
