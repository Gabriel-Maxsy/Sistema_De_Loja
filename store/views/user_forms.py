from django.shortcuts import render, redirect
from django.contrib import auth, messages
from store.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário salvo')
            return redirect('store:login')

    return render(
        request,
        'store/register.html',
        {
            'form': form
        }
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('store:index')
        
        messages.error(request, 'Login inválido')

    return render(
        request,
        'store/login.html',
        {
            'form': form
        }
    )


def logout_view(request):
    auth.logout(request)
    return redirect('store:login')