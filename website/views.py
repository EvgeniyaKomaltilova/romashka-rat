from django.shortcuts import render
from website.models import New, Image


def index(request):
    news = New.objects.filter(public='True').order_by('-date')[:3]
    image = Image.objects.filter(public='True').order_by('-date').first
    context = {'news': news, 'image': image}
    return render(request, 'website/index.html', context)


def archive(request):
    news = New.objects.filter(public='True').order_by('-date')
    context = {'news': news}
    return render(request, 'website/archive.html', context)
