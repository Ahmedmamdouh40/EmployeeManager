from django import forms
from .models import Employee,Contract,Department,Position
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeeForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = UserCreationForm.Meta.fields+(
            'full_name',
            'email',
            'emp_number',
            'gender',
            'date_of_birth',
            'nationality',
            'place_of_birth',
            'address',
            'mobile_number',
            'id_type',
            'id_number',
            'hire_date',
            'leave_balance',
            'manager',
            'social_status',
            'is_insured',
            'has_medical'
        )
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

