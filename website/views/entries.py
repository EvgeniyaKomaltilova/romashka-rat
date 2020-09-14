from django.shortcuts import render

from rattery.models.Rat import Rat
from website.models.Image import Image
from website.models.Entry import Entry
from itertools import chain


def main_page(request):
    """Домашняя страница со списком последних новостей и ссылкой на свободных крысят"""
    news = Entry.objects.filter(public='True').filter(topic='news').order_by('-date')[:3]
    image = Image.objects.filter(main_page=True).first
    available_rats = Rat.objects.filter(public='True').filter(status='available')
    context = {'news': news, 'image': image, 'rats': available_rats}
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


def contract(request):
    """Страница с договором на продажу крысенка"""
    entries = Entry.objects.filter(public=True).filter(topic='contract')
    context = {'entries': entries}
    return render(request, 'website/contract.html', context)


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
