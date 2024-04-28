from django.shortcuts import render, get_object_or_404
from .models import Item

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'detail.html', {
        'item': item
    })