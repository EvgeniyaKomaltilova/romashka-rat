from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('website.urls')),
    path('rats/', include('rattery.urls')),
    path('pdf/', include('pdf_generator.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
