from django.shortcuts import render, redirect
from .models import noteapp
from .forms import NoteForm


def noteapp_view(request):

    if request.method == 'POST':

        form = NoteForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/noteapp_view/')

    else:

        form = NoteForm()

        note = noteapp.objects.all()

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

    note = noteapp.objects.get(id=id)

    note.delete()

    return redirect('/noteapp_view/')


def update_note(request, id):

    note = noteapp.objects.get(id=id)

    if request.method == 'POST':

        form = NoteForm(request.POST, instance=note)

        if form.is_valid():

            form.save()

            return redirect('/noteapp_view/')

    else:

        form = NoteForm(instance=note)

    return render(request, 'update.html', {
        'form': form
    })