from django.urls import path

from . import views

urlpatterns = [
    path('view_students', views.view_students, name='student'),
]
