from django.urls import path

from . import views

urlpatterns = [
    path('students', views.students, name='student'),
    path("students/delete/<int:id>", views.delete_student, name='delete'),
    path('students_json', views.students_json, name='student'),

]
