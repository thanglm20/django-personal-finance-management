from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="preferences"),
    path('delete_category/<slug:id>/', views.delete_category, name="preferences-delete_category"),
    path('delete_source/<slug:id>/', views.delete_source, name="preferences-delete_source")

]
