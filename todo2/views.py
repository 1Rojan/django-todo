from django.shortcuts import render, HttpResponseRedirect, redirect
from . models import TodoList
from .forms import todoListForm


def index_template(request):
    lists = TodoList.objects.all()
    form = todoListForm()
    context = {'lists': lists, 'form': form}

    if request.method == 'POST':
        form = todoListForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/todo2')

    return render(request,'index_template.html', context )


def edit_template(request, pk):
    item  = TodoList.objects.get(id = pk)
    form = todoListForm(instance= item)
    if request.method == 'POST':
        form = todoListForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return  HttpResponseRedirect('/todo2')

    context = {
        'item': item,
        'form': form
    }
    return render(request, 'edit_template.html', context)


def delete_template(request, pk):
    item = TodoList.objects.get(id = pk)
    item.delete()
    return redirect('/todo2')
    # return render(request, 'delete_template.html')