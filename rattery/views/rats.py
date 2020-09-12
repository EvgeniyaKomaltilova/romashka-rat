from django.shortcuts import render
from itertools import chain

from rattery.models.Litter import Litter
from rattery.models.Rat import Rat


def available(request):
    """Страница со свободными крысятами"""
    available_rats = Rat.objects.filter(public='True', status='available')
    context = {'rats': available_rats}
    return render(request, 'rattery/available.html', context)


def male_rats(request):
    """Список всех крыс-самцов питомника"""
    rats = Rat.objects.filter(public=True, in_rattery=True, gender='male').order_by('-date_of_birth')
    alive_rats = rats.filter(alive=True)
    dead_rats = rats.filter(alive=False)
    context = {'alive_rats': alive_rats, 'dead_rats': dead_rats}
    return render(request, 'rattery/male_rats.html', context)


def female_rats(request):
    """Список всех крыс-самок питомника"""
    rats = Rat.objects.filter(public=True, in_rattery=True, gender='female').order_by('-date_of_birth')
    alive_rats = rats.filter(alive=True)
    dead_rats = rats.filter(alive=False)
    context = {'alive_rats': alive_rats, 'dead_rats': dead_rats}
    return render(request, 'rattery/female_rats.html', context)


def rat(request, rat_id):
    """Персональная страница крысы"""
    rat_object = Rat.objects.get(id=rat_id)
    context = {'rat': rat_object}
    return render(request, 'rattery/rat.html', context)


def litters(request, litter_year):
    """Список всех пометов питомника"""
    litters_list = Litter.objects.filter(public=True, year=litter_year).order_by('-date_of_birth')
    litter_years = []
    for litter in Litter.objects.order_by('date_of_birth'):
        if litter.year not in litter_years:
            litter_years.append(litter.year)
    context = {'litters': litters_list, 'years': litter_years}
    return render(request, 'rattery/litters.html', context)


def litter(request, litter_year, litter_id):
    """Страница конкретной литеры"""
    litter_object = Litter.objects.get(year=litter_year, id=litter_id)
    males = litter_object.children.filter(gender='male')
    females = litter_object.children.filter(gender='female')
    context = {'litter': litter_object, 'males': males, 'females': females}
    return render(request, 'rattery/litter.html', context)
