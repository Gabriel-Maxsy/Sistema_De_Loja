from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from store.models import Product
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name', 'price', 'description', 'price', 'amount',
        )

def create(request):
    if request.method == 'POST':

        context = {
            'form': ProductForm(request.POST)
        }

        return render(
            request,
            'store/create.html',
            context
        )

    context = {
        'form': ProductForm()
    }

    return render(
        request,
        'store/create.html',
        context
    )