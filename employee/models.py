from django.db import models
from enum import Enum

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
    
    SocialStatusChoices=[
        ('SINGLE' , 'Single'),
        ('MARRIED' , 'Married')
    ]
    social_status = models.CharField(choices=SocialStatusChoices , max_length=10)
    is_insured = models.BooleanField()
    is_active = models.BooleanField()
    has_medical = models.BooleanField()