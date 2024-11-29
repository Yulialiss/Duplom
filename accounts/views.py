from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import RoleForm

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def welcome_view(request):
    if request.method == 'POST':
        return redirect('choose_role')
    return render(request, 'accounts/welcome.html')

def choose_role_view(request):
    if 'role' not in request.session:
        if request.method == 'POST':
            form = RoleForm(request.POST)
            if form.is_valid():
                request.session['role'] = form.cleaned_data['role']
                return redirect('register')
        else:
            form = RoleForm()
        return render(request, 'accounts/choose_role.html', {'form': form})
    return redirect('register')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Реєстрація успішна!')
            return redirect('user_profile')
        else:
            messages.error(request, 'Помилка при реєстрації. Спробуйте ще раз.')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register_user'
                           '.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.is_staff or user.is_superuser:
                return redirect('admin_home')
            else:
                messages.success(request, 'Ви успішно увійшли!')
                return redirect('home')
        else:
            messages.error(request, 'Неправильний логін або пароль.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'Ви вийшли з системи.')
    return redirect('home')
