from django.urls import path
from website.views import entries

urlpatterns = [
    path('', entries.main_page, name='index'),
    path('about/', entries.about, name='about'),
    path('archive/', entries.archive, name='archive'),
    path('varieties/', entries.varieties, name='varieties'),
    path('colors/', entries.colors, name='colors'),
    path('markings/', entries.markings, name='markings'),
]
