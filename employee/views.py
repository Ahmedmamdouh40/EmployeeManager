from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Employee,Department,Contract,Position
from .forms import EmployeeForm ,PositionForm , DepartmentForm , ContractForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

######### Employee CRUD #########

@login_required
def create_employee(request):
    form = EmployeeForm
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees')
    return render(request , 'employees/add_employee.html' , {'form':form})

@login_required
def employees_list(request):
    all_employees = Employee.objects.filter(is_superuser=0)
    context = {'employees' : all_employees}
    return render(request , 'employees/employees_list.html' , context)

@login_required
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

@login_required
def delete_employee(request , employee_id):
    employee = Employee.objects.get(id = employee_id)
    employee.delete()
    return HttpResponseRedirect('/employees')


######### Position CRUD #########

@login_required
def positions_list(request):
    all_positions = Position.objects.all()
    context = {'positions' : all_positions}
    return render(request , 'positions/positions_list.html' , context)

@login_required
def create_position(request):
    form = PositionForm
    if request.method == "POST":
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees/positions')
    return render(request , 'positions/add_position.html' , {'form':form})

@login_required
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

@login_required
def delete_position(request , position_id):
    position = Position.objects.get(id = position_id)
    position.delete()
    return HttpResponseRedirect('/employees/positions')

######### Department CRUD #########

@login_required
def departments_list(request):
    all_departments = Department.objects.all()
    context = {'departments' : all_departments}
    return render(request , 'departments/departments_list.html' , context)

@login_required
def create_department(request):
    form = DepartmentForm
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees/departments')
    return render(request , 'departments/add_department.html' , {'form':form})

@login_required
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

@login_required
def delete_department(request , department_id):
    department = Department.objects.get(id = department_id)
    department.delete()
    return HttpResponseRedirect('/employees/departments')


######### Contract CRUD #########

@login_required
def contracts_list(request):
    all_contracts = Contract.objects.all()
    context = {'contracts' : all_contracts}
    return render(request , 'contracts/contracts_list.html' , context)

@login_required
def create_contract(request):
    form = ContractForm
    if request.method == "POST":
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees/contracts')
    return render(request , 'contracts/add_contract.html' , {'form':form})

@login_required
def edit_contract(request , contract_id):
    contract = get_object_or_404(Contract , id=contract_id)
    if request.method == "POST":
        form = ContractForm(request.POST , instance=contract)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees/contracts')
    else:
        form = ContractForm(instance=contract)
    return render(request , 'contracts/edit_contract.html' , {'form':form})

@login_required
def delete_contract(request , contract_id):
    contract = Contract.objects.get(id = contract_id)
    contract.delete()
    return HttpResponseRedirect('/employees/contracts')

