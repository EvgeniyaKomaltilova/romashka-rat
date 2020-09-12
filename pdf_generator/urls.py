from django.urls import path
from pdf_generator import views

urlpatterns = [
    path('rat/<int:data>/', views.rat_pedigree_view, name='rat_pedigree'),
    path('litter/<int:data>/', views.litter_pedigree_view, name='litter_pedigree')
    ]
