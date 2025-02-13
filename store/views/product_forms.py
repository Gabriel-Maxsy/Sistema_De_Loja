from store.forms import ProductForm
from django.shortcuts import get_object_or_404, redirect, render

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