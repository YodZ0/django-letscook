from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request=request, message='Login success!')
                return redirect(to='cabinet')
            else:
                messages.error(request=request, message='Invalid data. Please try again.')
    else:
        form = LoginForm()
    return render(request=request, template_name='authapp/login-page.html', context={'form': form})


def logout_user(request):
    logout(request)
    messages.info(request=request, message='You have logged out.')
    return redirect('login')


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request=request, message='Register success!')
            return redirect(to='login')
        else:
            messages.error(request=request, message='Invalid data. Please try again.')
            form = RegisterForm(request.POST)
    else:
        form = RegisterForm()

    return render(request=request, template_name='authapp/register-page.html', context={'form': form})
