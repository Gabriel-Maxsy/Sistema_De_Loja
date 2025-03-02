from django.shortcuts import render, redirect
from django.contrib import messages
from store.forms import RegisterForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário salvo')
            return redirect('store:index')

    return render(
        request,
        'store/register.html',
        {
            'form': form
        }
    )