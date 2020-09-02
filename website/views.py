from django.shortcuts import render
from website.models import New, Image, Rat

from itertools import chain


def index(request):
    news = New.objects.filter(public='True').order_by('-date')[:3]
    image = Image.objects.filter(public='True').order_by('-date').first
    context = {'news': news, 'image': image}
    return render(request, 'website/index.html', context)


def archive(request):
    news = New.objects.filter(public='True').order_by('-date')
    context = {'news': news}
    return render(request, 'website/archive.html', context)


def available(request):
    available_rats = Rat.objects.filter(public='True').filter(status='свободен')
    reserved_rats = Rat.objects.filter(public='True').filter(status='зарезервирован')
    all_rats = chain(available_rats, reserved_rats)
    context = {'rats': all_rats}
    return render(request, 'website/available.html', context)


def rat(request, rat_id):
    this_rat = Rat.objects.get(id=rat_id)
    context = {'rat': this_rat}
    return render(request, 'website/rat.html', context)
