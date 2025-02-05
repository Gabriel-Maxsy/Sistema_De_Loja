from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from store.models import Product

def create(request):
    if request.method == 'POST':
        print()
        print(request.method)
        print(request.POST.get('name'))
        print(request.POST.get('description'))
        print()

    context = {

    }

    print()
    print(request.method)
    print()

    return render(
        request,
        'store/create.html',
        context
    )