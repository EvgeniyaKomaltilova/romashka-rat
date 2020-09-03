from django.urls import path, include
from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('archive/', views.archive, name='archive'),
    path('available/', views.available, name='available'),
    path('litters/', views.litters, name='litters'),
    path('litters/<int:litter_id>/', views.litter, name='litter'),
    path('rats/<int:rat_id>/', views.rat, name='rat'),
]
