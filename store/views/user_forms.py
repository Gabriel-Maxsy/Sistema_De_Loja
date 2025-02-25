from django.shortcuts import render

from store.forms import RegisterForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

    return render(
        request,
        'store/register.html',
        {
            'form': form
        }
    )