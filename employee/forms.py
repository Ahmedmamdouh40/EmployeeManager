from django import forms
from .models import Employee,Contract,Department,Position

class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            "date_of_birth":DateInput(),
            "hire_date":DateInput(),
        }

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = "__all__"


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = "__all__"
        widgets = {
            "contract_start_date":DateInput(),
            "contract_end_date":DateInput()
        }

