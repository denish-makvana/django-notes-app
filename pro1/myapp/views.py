from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from .models import noteapp
from .forms import NoteForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404 
from rest_framework.response import Response
from .serializers import noteappSerializer
from .models import noteapp
from rest_framework.decorators import api_view


@login_required
def noteapp_view(request):

    if request.method == 'POST':

        form = NoteForm(request.POST)

        if form.is_valid():

            note = form.save(commit=False)
            note.user = request.user
            note.save()

            return redirect('/noteapp_view/')

    else:

        form = NoteForm()

        note = noteapp.objects.filter(user=request.user)

        query = request.GET.get('query')

        if query:
             note = noteapp.objects.filter(
                 title__icontains=query
                   )
        return render(request,
    'noteapp.html', {
                  'note': note,
                  'form': form
            })


def delete_note(request, id):
    note = get_object_or_404(noteapp,id=id)
    note.delete()
    return redirect('/noteapp_view/')


def update_note(request, id):

    note = noteapp.objects.get(id=id)

    if request.method == 'POST':

        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            note=form.save(commit=False)
            note.user = request.user
            note.save()

            form.save()

            return redirect('/noteapp_view/')

    else:

        form = NoteForm(instance=note)

    return render(request, 'update.html', {
        'form': form
    })


def register(request):

    form = UserCreationForm()

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('/noteapp_view/')

    return render(request, 'register.html', {   
        'form': form
    })


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect('/noteapp_view/')
    return render(request, 'login_view.html')


def logout_view(request):
    logout(request)
    return redirect('/login_view/')


@api_view(['GET'])
def notes_api(request):

    notes = noteapp.objects.all()

    serializer = noteappSerializer(notes, many=True)
    
    return Response(serializer.data)