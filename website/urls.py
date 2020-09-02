from django.urls import path, include
from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('archive/', views.archive, name='archive'),
    path('available/', views.available, name='available'),
    path('rats/<int:rat_id>/', views.rat, name='rat'),
]
