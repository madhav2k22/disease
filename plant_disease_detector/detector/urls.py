# detector/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ImageUploadView

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
]
