from django import forms
from .models import LeaveMaster , EmployeeLeave

class DateInput(forms.DateInput):
    input_type = 'date'


class LeaveMasterForm(forms.ModelForm):
    class Meta:
        model = LeaveMaster
        fields = "__all__"


class EmployeeLeaveForm(forms.ModelForm):
    class Meta:
        model = EmployeeLeave
        fields = "__all__"
        widgets = {
            "start_date":DateInput(),
            "end_date":DateInput(),
            "resume_date":DateInput(),
        }