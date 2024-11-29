from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/update-avatar/', views.update_avatar, name='update_avatar'),
    path('profile/password-change/', views.password_change_view, name='password_change'),
]

