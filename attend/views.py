from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignupForm


def home(request):
    return render(request, 'attend/index.html', None)


def base(request):
    return render(request, 'attend/intro.html', None)


def feed(request):
    return render(request, 'attend/feedback.html', None)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(name=name, password=password)
            login(request, user)
            return redirect('attend/intro.html')

    else:
        form = SignupForm()
        return render(request, 'accounts/signup_form.html', {'form': form})
