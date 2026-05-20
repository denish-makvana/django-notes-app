from django.shortcuts import render
from .models import noteapp

# Create your views here.

def noteapp_view(request):
    note = noteapp.objects.all()

    return render(request,"noteapp.html",{'note':note})