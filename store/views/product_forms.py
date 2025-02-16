from store.forms import ProductForm
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from store.models import Product

def create(request):
    form_action = reverse('store:create')

    if request.method == 'POST':
        form = ProductForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action, 
        }

        if form.is_valid():
            product = form.save()
            return redirect('store:update', product_id=product.pk)

        return render(
            request,
            'store/create.html',
            context
        )

    context = {
        'form': ProductForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'store/create.html',
        context
    )

def update(request, product_id):
    product = get_object_or_404(
        Product, pk=product_id, 
    )
    form_action = reverse('store:update', args=(product_id,))

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        context = {
            'form': form,
            'form_action': form_action, 
        }

        if form.is_valid():
            product = form.save()
            return redirect('store:update', product_id=product.pk)

        return render(
            request,
            'store/create.html',
            context
        )

    context = {
        'form': ProductForm(instance=product),
        'form_action': form_action,
    }

    return render(
        request,
        'store/create.html',
        context
    )