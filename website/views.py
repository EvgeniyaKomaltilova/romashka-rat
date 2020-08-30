from django.shortcuts import render
from website.models import New


def index(request):
    news = New.objects.order_by('-date')
    context = {'news': news}
    return render(request, 'website/index.html', context)
