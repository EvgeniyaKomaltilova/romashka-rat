from django.shortcuts import render
from website.models import Image, Rat, Entry, Litter
from itertools import chain


def index(request):
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


def available(request):
    available_rats = Rat.objects.filter(public='True').filter(status='свободен')
    reserved_rats = Rat.objects.filter(public='True').filter(status='зарезервирован')
    all_rats = chain(available_rats, reserved_rats)
    context = {'rats': all_rats}
    return render(request, 'website/available.html', context)


def rats(request):
    rats_list = Rat.objects.filter(public=True).filter(in_rattery=True)
    males = rats_list.filter(gender='male').order_by('-date_of_birth')
    females = rats_list.filter(gender='female').order_by('-date_of_birth')
    context = {'rats': rats_list, 'males': males, 'females': females}
    return render(request, 'website/rats.html', context)


def rat(request, rat_id):
    rat_object = Rat.objects.get(id=rat_id)
    context = {'rat': rat_object}
    return render(request, 'website/rat.html', context)


def litters(request):
    litters_list = Litter.objects.filter(public=True).order_by('-date_of_birth')
    context = {'litters': litters_list}
    return render(request, 'website/litters.html', context)


def litter(request, litter_id):
    litter_object = Litter.objects.get(id=litter_id)
    males = litter_object.children.filter(gender='male')
    females = litter_object.children.filter(gender='female')
    context = {'litter': litter_object, 'males': males, 'females': females}
    return render(request, 'website/litter.html', context)
