from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .forms import ItemForm
from django.shortcuts import redirect

# Create your views here.


def index(request):
    list_item = models.Item.objects.all()
    context = {
        "item": list_item
    }
    return render(request, 'food/index.html', context)


def details(request, id):
    item = models.Item.objects.get(id=id)

    return render(request, 'food/details.html', {'item': item})


def addItem(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/forms.html', {'form': form})


def updateItem(request, id):
    item = models.Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/forms.html', {'item': item, 'form': form})


def deleteItem(request, id):
    item = models.Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/delete.html', {'item': item})
