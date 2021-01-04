from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import LeaveMaster, EmployeeLeave
from employee.models import Employee
from .forms import LeaveMasterForm ,EmployeeLeaveForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import datetime

######### LeaveMaster CRUD #########

def leave_masters_list(request):
    all_leave_masters = LeaveMaster.objects.all()
    context = {'leave_masters' : all_leave_masters}
    return render(request , 'leave_master/leave_masters_list.html' , context)

def create_leave_master(request):
    form = LeaveMasterForm
    if request.method == "POST":
        form = LeaveMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/leaves')
    return render(request , 'leave_master/add_leave_master.html' , {'form':form})

def edit_leave_master(request , leave_master_id):
    leave_master = get_object_or_404(LeaveMaster , id=leave_master_id)
    if request.method == "POST":
        form = LeaveMasterForm(request.POST , instance=leave_master)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/leaves')
    else:
        form = LeaveMasterForm(instance=leave_master)
    return render(request , 'leave_master/edit_leave_master.html' , {'form':form}) 

def delete_leave_master(request , leave_master_id):
    leave_master = LeaveMaster.objects.get(id = leave_master_id)
    leave_master.delete()
    return HttpResponseRedirect('/leaves')


######### EmployeeLeave CRUD #########

def employee_leaves_list(request):
    all_employee_leaves = EmployeeLeave.objects.all()
    context = {'employee_leaves' : all_employee_leaves}
    return render(request , 'employee_leaves/employee_leaves_list.html' , context)


def create_employee_leave(request):
    form = EmployeeLeaveForm
    if request.method == "POST":
        form = EmployeeLeaveForm(request.POST)
        emp_id = form.data['emp_name']
        leave_type = form.data['leave_type']
        start_date = datetime.strptime(form.data['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(form.data['end_date'], '%Y-%m-%d')
        leave_value = EmployeeLeave.detect_leave_value_due_to_type(leave_type)
        if form.is_valid():
            if EmployeeLeave.is_in_a_leave(emp_id) == False:
                if EmployeeLeave.is_leave_balance_valid(emp_id,leave_value,start_date,end_date)== True:
                    form.save()
                    return HttpResponseRedirect('/leaves/employee_leaves')
                else:
                    messages.error(request , 'You do not have enough balance for this leave')
            else:
                messages.error(request, 'You can not ask for a new leave while you are in another leave')
    return render(request , 'employee_leaves/add_employee_leave.html' , {'form':form})


def edit_employee_leave(request , employee_leave_id):
    employee_leave = get_object_or_404(EmployeeLeave , id=employee_leave_id)
    if request.method == "POST":
        form = EmployeeLeaveForm(request.POST , instance=employee_leave)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/leaves/employee_leaves')
    else:
        form = EmployeeLeaveForm(instance=employee_leave )
    return render(request , 'employee_leaves/edit_employee_leave.html' , {'form':form})

def delete_employee_leave(request , employee_leave_id):
    employee_leave = EmployeeLeave.objects.get(id = employee_leave_id)
    employee_leave.delete()
    return HttpResponseRedirect('/leaves/employee_leaves')


