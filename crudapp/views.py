from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Crud

from .forms import CrudForm

def index_view(request):
    cruds = Crud.objects.all()

    if request.method == "POST":
        form = CrudForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/crud')

    forms = CrudForm()
    context = {
        'cruds': cruds,
        'form': forms
    }
    return render(request, 'index_view.html', context)

def edit(request, pk):
    list = Crud.objects.get(id = pk)

    if request.method == "POST":
        form = CrudForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
        return redirect('/crud')

    form = CrudForm(instance=list)
    context = {
        'form': form
    }
    return render(request, 'edit.html', context)

def delete(request, pk):
    list = Crud.objects.get(id= pk)
    if request.method == 'POST':
        list.delete()
        return redirect('/crud')
    context = {
        'list': list
    }
    return render(request, 'delete.html', context)
    if request.method == 'POST':
        form = CrudForm(list)
