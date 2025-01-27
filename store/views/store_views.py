from django.shortcuts import render
from store.models import Product
from django.shortcuts import get_object_or_404, render

def index(request):
    products = Product.objects.all().order_by('-id')[:10]
    
    context = {
        'products': products,
        'site_title': 'Products - ',
    }

    return render(
        request,
        'store/index.html',
        context
    )

def product(request, product_id):
    # single_product = Product.objects.filter(pk=product_id).first()
    single_product = get_object_or_404(
        Product, pk=product_id
    )
    context = {
        'product': single_product,
        'site_title': f'{single_product.name} - '
    }
    return render(
        request,
        'store/product.html',
        context
    )