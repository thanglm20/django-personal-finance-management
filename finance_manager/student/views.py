from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TblStudents

# Create your views here.

def view_students(request):
    students = TblStudents.objects.all()
    template = loader.get_template('view_students.html')

    context = {
        "students": students
    }
    # print(students)
    return HttpResponse(template.render(context, request))