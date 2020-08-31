from django.shortcuts import render
from website.models import New


def index(request):
    news = New.objects.filter(public='True').order_by('-date')[:3]
    context = {'news': news}
    return render(request, 'website/index.html', context)
