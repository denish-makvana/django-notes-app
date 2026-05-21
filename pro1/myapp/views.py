from django.shortcuts import render,redirect
from .models import noteapp

# Create your views here.

def noteapp_view(request):
        if request.method == 'POST':
            title=request.POST.get('title')
            description=request.POST.get('description')
            noteapp.objects.create(title=title,description=description)

            return redirect('/noteapp_view/')
        
        notes = noteapp.objects.all()
        return render(request,"noteapp.html",{'notes':notes})


def delete(request,id):
      
      notes=noteapp.objects.get(id=id)
      notes.delete()
      return redirect('/noteapp_view/')
      