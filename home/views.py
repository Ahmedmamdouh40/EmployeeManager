from django.shortcuts import render
from leave.models import EmployeeLeave
from django.contrib.auth.decorators import login_required

@login_required
def view_leaves(request):
    all_leaves = EmployeeLeave.objects.all()
    context = {'leaves' : all_leaves}
    return render(request , 'employee_leaves_list.html' , context)

