from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


def index(request):
    items = Item.objects.all()
    form = ItemForm()


    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/todo')

    context = {'datasets': items, 'form': form}
    return render(request, 'index_view.html', context)

def edit_view(request, pk):
    item= Item.objects.get(id=pk)
    form = ItemForm(instance=item )
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/todo')

    return render(request, 'edit_view.html', context)

def delete_view(request, pk):
    item= Item.objects.get(id=pk)
    context = {
    'item': item
    }
    if request.method == 'POST':
        item.delete()
        return redirect('/todo')

    return render(request, 'delete_view.html', context)
