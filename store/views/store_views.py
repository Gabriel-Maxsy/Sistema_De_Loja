from django.shortcuts import render
from store.models import Product

def index(request):
    products = Product.objects.all().order_by('-id')[:10]
    
    context = {
        'products': products,
    }

    return render(
        request,
        'store/index.html',
        context
    )