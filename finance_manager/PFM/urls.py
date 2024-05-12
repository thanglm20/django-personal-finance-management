from django.urls import path

from . import views

urlpatterns = [
    path('pfm', views.index, name='PFM'),
]
