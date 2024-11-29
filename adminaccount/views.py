from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_home(request):
    return render(request, 'adminaccount/admin_home.html')