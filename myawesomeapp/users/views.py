from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, ImageCreationForm


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, 'Congratulation %s your account has been created!' % username)
            login(request, user)
            return redirect('home')

    else:
        form = RegistrationForm()
        return render(request, 'users/registration.html', {'form': form})


def logout(request):
    messages.info(request, 'You have been logged out from your account!')
    return redirect('home')
# Create your views here.
