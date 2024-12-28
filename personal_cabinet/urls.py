from django.urls import path
from . import views
app_name = 'personal_cabinet'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('settings/', views.settings_page, name='settings'),

]
