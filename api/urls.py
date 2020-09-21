from django.urls import path
from api.views import RatView, LitterView

app_name = "api"

urlpatterns = [
    path('rats/', RatView.as_view(), name='rat_api'),
    path('litters/', LitterView.as_view(), name='litter_api'),
]