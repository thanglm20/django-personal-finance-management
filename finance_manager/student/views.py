from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import TblStudents
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models.functions import JSONObject
from django.core.serializers import serialize
# Create your views here.


@csrf_exempt
def students(request):
    if request.method == "GET":
        print("Getting students")
        students = TblStudents.objects.all()
        template = loader.get_template('view_students.html')

        context = {
            "students": students
        }
        # print(students)
        return HttpResponse(template.render(context, request))
    elif request.method == "POST":
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            print(body)
            student = TblStudents(
                id_std = body['id'],
                name_std = body['name'],
                sex = body['sex'],
                class_id = body['class_id'],
                hometown = body['hometown'],
                birthday = body['birthday'])
            student.save()        
        except ValueError:
            return HttpResponse(status=400)
        return HttpResponse(status=200)
    elif request.method == "PUT":
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            id_std = body['id']
            print(id_std)
            student = TblStudents.objects.get(pk=id_std)   
            # student = TblStudents.objects.filter(id_std=id_std)   
            if student is None:
                return HttpResponse(status=400)
            student.name_std = body['name']
            student.sex = body['sex']
            student.class_id = body['class_id']
            student.hometown = body['hometown']
            student.birthday = body['birthday']                
            student.save()
        except ValueError:
            return HttpResponse(status=400)
        return HttpResponse(status=200)
        
def students_json(request):
    if request.method == "GET":
        print("Getting students")
        students = TblStudents.objects.all()
        template = loader.get_template('view_students.html')
        context = {
            "students": students
        }
        data = list(students.values())

        print((data))
        return JsonResponse(data, safe=False)
      
@csrf_exempt
def delete_student(request, id):
    print("Deleting student: ", id)
    student = TblStudents.objects.get(pk=id)
    student.delete()
    # return HttpResponse(status=200)
    return redirect(students)


    