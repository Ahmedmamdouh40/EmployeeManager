from django.db import models
from datetime import datetime    


class Employee (models.Model):
    full_name = models.CharField(max_length=150)
    emp_number = models.IntegerField()
    
    GenderChoices=[
        ('M' , 'Male'),
        ('F' , 'Female')
    ]
    gender = models.CharField(choices=GenderChoices , max_length=1)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    place_of_birth = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=150)
    
    IdTypeChoices=[
        ('NATIONAL' , 'National'),
        ('PASSPORT' , 'Passport')
    ]
    id_type = models.CharField(choices=IdTypeChoices , max_length=10)
    id_number = models.CharField(max_length=14)
    hire_date = models.DateField()
    leave_balance = models.IntegerField(default=21)
    
    SocialStatusChoices=[
        ('SINGLE' , 'Single'),
        ('MARRIED' , 'Married')
    ]
    social_status = models.CharField(choices=SocialStatusChoices , max_length=10)
    is_insured = models.BooleanField()
    is_active = models.BooleanField()
    has_medical = models.BooleanField()

    def __str__(self):
        return self.full_name


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
    emp_name = models.ForeignKey(Employee , on_delete=models.CASCADE ,  related_name='%(class)s_requests_created')
    position = models.ForeignKey(Position , on_delete=models.CASCADE)
    department = models.ForeignKey(Department ,on_delete=models.CASCADE)
    manager = models.ForeignKey(Employee , on_delete=models.CASCADE)

    ContratTypeChoices = [
        ('CASUAL' , 'Casual'),
        ('TRAINEE' , 'Trainee'),
        ('CONTRACTOR' , 'Contractor')
    ]
    contract_type = models.CharField(choices=ContratTypeChoices , max_length=15)
    contract_start_date = models.DateField(default=datetime.now)
    contract_end_date = models.DateField(null=True , blank=True) 
    def __str__(self):
        return self.emp_name.full_name

    