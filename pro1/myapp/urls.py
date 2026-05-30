from django.contrib import admin
from django.urls import path,include
from .import views
from .views import notes_api

urlpatterns = [
  
    path('noteapp_view/',views.noteapp_view,name='noteapp_view'),
    path('delete_note/<int:id>/',views.delete_note,name='delete_note'),
    path('update_note/<int:id>/',views.update_note,name='update_note'),
    path('register/',views.register,name='register'),
    path('login_view/',views.login_view,name='login_view'),
    path('logout_view/',views.logout_view,name='logout_view'),
    path('api/notes/',notes_api),
    

]