from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('main.urls')),
    path('user/', include('useraccount.urls')),
    path('adminaccount/', include('adminaccount.urls')),

]
