from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
     path('', views.index, name="expenses"),
     path('add', views.add_expense, name="expenses-add"),
     path('edit/<int:id>', views.edit_expense, name="expenses-edit"),
     path('delete/<int:id>', views.delete_expense, name="expenses-delete"),
     path('search', csrf_exempt(views.search_expenses), name="expenses-search"),
     path('category_summary', views.expense_category_summary, name="expenses-category_summary"),
     path('stats', views.stats_view, name="expenses-stats"),
     path('export_csv', views.export_csv, name="expenses-export_csv"),
     path('export_pdf', views.export_pdf, name="expenses-export_pdf"),
]
