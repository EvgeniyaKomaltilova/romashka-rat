from django.urls import path
from website.views import entries
from website.views import rats

urlpatterns = [
    path('', entries.main_page, name='index'),
    path('about/', entries.about, name='about'),
    path('archive/', entries.archive, name='archive'),
    path('available/', rats.available, name='available'),
    path('litters/', rats.litters, name='litters'),
    path('litters/<int:litter_id>/', rats.litter, name='litter'),
    path('rats/', rats.rats, name='rats'),
    path('rats/<int:rat_id>/', rats.rat, name='rat'),
]
