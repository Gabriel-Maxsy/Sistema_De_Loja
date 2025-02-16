from store.forms import ProductForm
from django.shortcuts import redirect, render

def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        context = {
            'form': form 
        }

        if form.is_valid():
            form.save()
            return redirect('store:create')

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