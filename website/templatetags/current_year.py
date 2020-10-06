from datetime import date
from django import template

register = template.Library()


@register.simple_tag()
def current_year():
    return date.today().year
