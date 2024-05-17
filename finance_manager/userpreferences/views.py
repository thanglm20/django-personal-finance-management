from django.shortcuts import render, redirect
import os
import json
from django.conf import settings
from .models import UserPreference
from django.contrib import messages
from userincome.models import Source
from expenses.models import Category
# Create your views here.


def index(request):
    currency_data = []
    file_path = os.path.join(settings.BASE_DIR, 'currencies.json')

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        for k, v in data.items():
            currency_data.append({'name': k, 'value': v})

    exists = UserPreference.objects.filter(user=request.user).exists()
    user_preferences = None
    if exists:
        user_preferences = UserPreference.objects.get(user=request.user)
    categories = Category.objects.all()
    sources = Source.objects.all()
    if request.method == "POST":
        if 'currency'in request.POST:
            currency = request.POST['currency']
            if exists:
                user_preferences.currency = currency
                user_preferences.save()
            else:
                UserPreference.objects.create(user=request.user, currency=currency)
            messages.success(request, 'Saved currency successfully')

        elif 'expense_category' in request.POST:
            category = request.POST['expense_category']
            exists = Category.objects.filter(name=category).exists()
            if exists:
                messages.error(request, 'This category existed')
            elif  category == "":
                messages.error(request, 'The category is not empty')
            else:
                Category.objects.create(name=category)
                messages.success(request, 'Saved expense catogories successfully')  
        elif 'source_income' in request.POST:
            source = request.POST['source_income']
            exists = Source.objects.filter(name=source).exists()
            if exists :
                messages.error(request, 'This source existed')
            elif source == "":
                messages.error(request, 'The source income is not empty')
            else:
                Source.objects.create(name=source)
                messages.success(request, 'Saved source income successfully')

    return render(request, 'preferences/index.html',{'currencies': currency_data,
                                                    'user_preferences': user_preferences,
                                                    'categories': categories,
                                                    'sources': sources})

def delete_category(request, id):
    cate = Category.objects.get(id=id)
    if cate:
        cate.delete()
        messages.success(request, 'Removed category')
    return redirect('preferences')

def delete_source(request, id):
    src = Source.objects.get(id=id)
    if src:
        src.delete()
        messages.success(request, 'Removed source')
    return redirect('preferences')
