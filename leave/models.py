from django.db import models
from employee.models import Employee

class LeaveMaster(models.Model):
    name = models.CharField(max_length=20)
    value = models.FloatField()

    def __str__(self):
        return self.name

class EmployeeLeave(models.Model):
    emp_name = models.ForeignKey(Employee , on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    resume_date = models.DateField()
    leave_type = models.ForeignKey(LeaveMaster , on_delete=models.CASCADE)


    def __str__(self):
        return self.emp_name.full_name
