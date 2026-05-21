from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
  
    path('noteapp_view/',views.noteapp_view,name='noteapp_view'),
    path('delete/<int:id>/',views.delete,name='delete'),


]