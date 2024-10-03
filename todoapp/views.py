from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpRequest

#importing forms and models
from .models import Notes
from .forms import NotesForm

# Create your views here.

def home(request):
    item_list = Notes.objects.order_by("priority_level","-date")
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo')
    else:
        form = NotesForm()

    page = {
        "form": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/todo.html', page)

def delete_note(request,item_id):
    if request.method == "POST":
        note = Notes.objects.get(id = item_id)
        note.delete()

    return redirect('/todo')