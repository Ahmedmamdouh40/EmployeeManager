from django.db import models
from employee.models import Employee

class Department(models.Model):
    name = models.CharField(max_length=50)
    department_desc = models.ForeignKey('self' ,on_delete=models.CASCADE ,blank=True, null=True)
    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Contract(models.Model):
    emp_name = models.ForeignKey(Employee , on_delete=models.CASCADE)
    position = models.ForeignKey(Position , on_delete=models.CASCADE)
    
    