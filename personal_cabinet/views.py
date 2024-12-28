from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm, UserEditForm
from .models import Profile

@login_required
def settings_page(request):
    return render(request, 'personal_cabinet/settings.html')

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('personal_cabinet:dashboard')
        else:
            return render(
                request,
                'personal_cabinet/edit_profile.html',
                {
                    'user_form': user_form,
                    'profile_form': profile_form,
                    'errors': {
                        'user_form_errors': user_form.errors,
                        'profile_form_errors': profile_form.errors,
                    }
                }
            )
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile)

    return render(
        request,
        'personal_cabinet/edit_profile.html',
        {'user_form': user_form, 'profile_form': profile_form}
    )

@login_required
def dashboard(request):
    return render(request, 'personal_cabinet/dashboard.html')
