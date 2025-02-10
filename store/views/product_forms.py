from typing import Any, Dict
from django.core.exceptions import ValidationError
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

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            'name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )

        self.add_error(
            'name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )
        
        return super().clean()

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