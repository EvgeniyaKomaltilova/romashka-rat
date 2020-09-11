from django.shortcuts import render

from rattery.models.Rat import Rat
from website.models.Image import Image
from website.models.Entry import Entry
from itertools import chain


def main_page(request):
    """Домашняя страница со списком последних новостей и ссылкой на свободных крысят"""
    news = Entry.objects.filter(public='True').filter(topic='news').order_by('-date')[:3]
    image = Image.objects.get(main_page=True)
    available_rats = Rat.objects.filter(public='True').filter(status='available')
    reserved_rats = Rat.objects.filter(public='True').filter(status='reserved')
    all_rats = chain(available_rats, reserved_rats)
    context = {'news': news, 'image': image, 'rats': all_rats}
    return render(request, 'website/index.html', context)


def about(request):
    """Страница с информацией о питомнике"""
    entries = Entry.objects.filter(public=True).filter(topic='about')
    context = {'entries': entries}
    return render(request, 'website/about.html', context)


def archive(request):
    """Страница со всеми новостями в хронологическом порядке"""
    news = Entry.objects.filter(public='True').filter(topic='news').order_by('-date')
    context = {'news': news}
    return render(request, 'website/archive.html', context)


def varieties(request):
    """Страница с информацией о разновидностях крыс"""
    entries = Entry.objects.filter(public=True).filter(topic='varieties')
    context = {'entries': entries}
    return render(request, 'website/varieties.html', context)


def colors(request):
    """Страница с информацией о разновидностях крыс"""
    entries = Entry.objects.filter(public=True).filter(topic='colors')
    context = {'entries': entries}
    return render(request, 'website/colors.html', context)


def markings(request):
    """Страница с информацией о разновидностях крыс"""
    entries = Entry.objects.filter(public=True).filter(topic='markings')
    context = {'entries': entries}
    return render(request, 'website/markings.html', context)
