from django.shortcuts import render
from website.models.Image import Image
from website.models.Rat import Rat
from website.models.Entry import Entry
from itertools import chain


def main_page(request):
    news = Entry.objects.filter(public='True').filter(topic='news').order_by('-date')[:3]
    image = Image.objects.filter(rat=None).order_by('-date').first
    available_rats = Rat.objects.filter(public='True').filter(status='свободен')
    reserved_rats = Rat.objects.filter(public='True').filter(status='зарезервирован')
    all_rats = chain(available_rats, reserved_rats)
    context = {'news': news, 'image': image, 'rats': all_rats}
    return render(request, 'website/index.html', context)


def about(request):
    entries = Entry.objects.filter(public=True).filter(topic='about')
    context = {'entries': entries}
    return render(request, 'website/about.html', context)


def archive(request):
    news = Entry.objects.filter(public='True').filter(topic='news').order_by('-date')
    context = {'news': news}
    return render(request, 'website/archive.html', context)