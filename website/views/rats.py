from django.shortcuts import render
from website.models.Rat import Rat
from website.models.Litter import Litter
from itertools import chain


def available(request):
    """Страница со свободными крысятами"""
    available_rats = Rat.objects.filter(public='True').filter(status='свободен')
    reserved_rats = Rat.objects.filter(public='True').filter(status='зарезервирован')
    all_rats = chain(available_rats, reserved_rats)
    context = {'rats': all_rats}
    return render(request, 'website/available.html', context)


def rats(request):
    """Список всех крыс питомника"""
    rats_list = Rat.objects.filter(public=True).filter(in_rattery=True)
    males = rats_list.filter(gender='самец').order_by('-date_of_birth')
    females = rats_list.filter(gender='самка').order_by('-date_of_birth')
    context = {'rats': rats_list, 'males': males, 'females': females}
    return render(request, 'website/rats.html', context)


def rat(request, rat_id):
    """Персональная страница крысы"""
    rat_object = Rat.objects.get(id=rat_id)
    context = {'rat': rat_object}
    return render(request, 'website/rat.html', context)


def litters(request):
    """Список всех пометов питомника"""
    litters_list = Litter.objects.filter(public=True).order_by('-date_of_birth')
    context = {'litters': litters_list}
    return render(request, 'website/litters.html', context)


def litter(request, litter_id):
    """Страница конкретной литеры"""
    litter_object = Litter.objects.get(id=litter_id)
    males = litter_object.children.filter(gender='самец')
    females = litter_object.children.filter(gender='самка')
    context = {'litter': litter_object, 'males': males, 'females': females}
    return render(request, 'website/litter.html', context)
