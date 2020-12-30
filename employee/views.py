from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Employee,Department,Contract,Position
from .forms import EmployeeForm ,PositionForm , DepartmentForm
from django.http import HttpResponseRedirect

######### Employee CRUD #########

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


######### Position CRUD #########

def positions_list(request):
    all_positions = Position.objects.all()
    context = {'positions' : all_positions}
    return render(request , 'positions/positions_list.html' , context)

def create_position(request):
    form = PositionForm
    if request.method == "POST":
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees/positions')
    return render(request , 'positions/add_position.html' , {'form':form})

def edit_position(request , position_id):
    position = get_object_or_404(Position , id=position_id)
    if request.method == "POST":
        form = PositionForm(request.POST , instance=position)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees/positions')
    else:
        form = PositionForm(instance=position)
    return render(request , 'positions/edit_position.html' , {'form':form})

def delete_position(request , position_id):
    position = Position.objects.get(id = position_id)
    position.delete()
    return HttpResponseRedirect('/employees/positions')

######### Department CRUD #########

def departments_list(request):
    all_departments = Department.objects.all()
    context = {'departments' : all_departments}
    return render(request , 'departments/departments_list.html' , context)

def create_department(request):
    form = DepartmentForm
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees/departments')
    return render(request , 'departments/add_department.html' , {'form':form})

def edit_department(request , department_id):
    department = get_object_or_404(Department , id=department_id)
    if request.method == "POST":
        form = DepartmentForm(request.POST , instance=department)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees/departments')
    else:
        form = DepartmentForm(instance=department)
    return render(request , 'departments/edit_department.html' , {'form':form})

def delete_department(request , department_id):
    department = Department.objects.get(id = department_id)
    department.delete()
    return HttpResponseRedirect('/employees/departments')

