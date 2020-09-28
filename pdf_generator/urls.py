from django.urls import path
from pdf_generator import views

urlpatterns = [
    path('litter/<int:data>/', views.litter_pedigree_view, name='litter_pedigree')
    ]
