from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from store.models import Product

def create(request):
    context = {

    }

    return render(
        request,
        'store/create.html',
        context
    )