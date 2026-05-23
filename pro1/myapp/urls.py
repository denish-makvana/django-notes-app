from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
  
    path('noteapp_view/',views.noteapp_view,name='noteapp_view'),
    path('delete_note/<int:id>/',views.delete_note,name='delete_note'),
    path('update_note/<int:id>/',views.update_note,name='update_note')

]