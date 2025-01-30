from store.models import Product
from django.db.models import Q
# from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

def index(request):
    products = Product.objects.order_by('-id')[:10]
    
    context = {
        'products': products,
        'site_title': 'Products - ',
    }

    return render(
        request,
        'store/index.html',
        context
    )

def search(request):             # Se o parâmetro "q" estiver vazio, retorne ''.
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('store:index')

    products = Product.objects \
        .filter(
            Q(name__icontains=search_value) |
            Q(category__name__icontains=search_value) |  # Busca pelo nome da categoria
            Q(owner__username__icontains=search_value)   # Busca pelo nome do usuário
        )\
        .order_by('-id')
    
    # # Redireciona se nenhum produto for encontrado (fiz de outra forma direto nos templates)
    # if not products.exists():
    #     messages.warning(request, f'O produto/categoria/fornecedor "{search_value}" não foi encontrado.')
    #     return redirect('store:index')
    
    context = {
        'products': products,
        'site_title': 'Search - ',
        'search_value': search_value,
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