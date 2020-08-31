from random import randint

from django.shortcuts import render
from website.models import New, Image


def index(request):
    news = New.objects.filter(public='True').order_by('-date')[:3]
    image = Image.objects.filter(public='True').order_by('-date').first
    context = {'news': news, 'image': image}
    return render(request, 'website/index.html', context)
