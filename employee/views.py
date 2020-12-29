from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Employee,Department,Contract,Position
from .forms import EmployeeForm
from django.http import HttpResponseRedirect


def create_employee(request):
    form = EmployeeForm
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees')
    return render(request , 'employees/add_employee.html' , {'form':form})

def employees_list(request):
    all_employees = Employee.objects.all()
    context = {'employees' : all_employees}
    return render(request , 'employees/employees_list.html' , context)

def edit_employee(request , employee_id):
    employee = get_object_or_404(Employee , id=employee_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST , instance=employee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request , 'employees/edit_employee.html' , {'form':form}) 

def delete_employee(request , employee_id):
    employee = Employee.objects.get(id = employee_id)
    employee.delete()
    return HttpResponseRedirect('/employees')