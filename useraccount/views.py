from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.shortcuts import render, redirect
from django.contrib import messages


@login_required
def update_avatar(request):
    if request.method == 'POST':
        if 'avatar' in request.FILES:
            print('Avatar file found:', request.FILES['avatar'])
            request.user.avatar = request.FILES['avatar']
            request.user.save()
            messages.success(request, 'Аватарку успішно оновлено!')
            return redirect('user_profile')
        else:
            print('No avatar file found')
            messages.error(request, 'Файл аватара не був переданий.')
    return redirect('user_profile')

@login_required
def user_profile(request):
    return render(request, 'useraccount/user_profile.html')

@login_required
def password_change_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Пароль успішно змінено!')
            return redirect('user_profile')
        else:
            messages.error(request, 'Помилка при зміні пароля.')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'useraccount/password_change.html', {'form': form})