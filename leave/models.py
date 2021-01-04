from django.db import models
from employee.models import Employee
from datetime import datetime

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

    LeaveStatusChoices = [
        ('WAITING' , 'Waiting'),
        ('APPROAVED' , 'Approaved'),
        ('REJECTED' , 'Rejected')
    ]
    leave_status = models.CharField(choices=LeaveStatusChoices , max_length=25 , default='WAITING')

    def calculate_number_of_leave_days(self):
        days = self.end_date - self.start_date
        return (days.days)
    
    def __str__(self):
        return self.emp_name.full_name
    
    def detect_leave_value_due_to_type(leave_type):
        leave_type = LeaveMaster.objects.get(id=leave_type)
        return leave_type.value

    def  is_in_a_leave(emp_id):
        emp_leaves = EmployeeLeave.objects.filter(emp_name = emp_id)
        if  len(emp_leaves) == 0: 
            return False
        else:
            emp_last_leave = emp_leaves.order_by('-id')[0]
            if emp_last_leave.start_date < datetime.now().date() and emp_last_leave.resume_date > datetime.now().date():
                return True
            else:
                return False


    def is_leave_balance_valid(emp_id ,leave_value,start_date,end_date):
        emp = Employee.objects.get(id = emp_id)
        emp_leaves_balance = emp.leave_balance
        requested_leave_period =  end_date - start_date
        requested_leave_value = requested_leave_period.days * leave_value
        print(end_date)
        if emp_leaves_balance >= requested_leave_value:
            return True
        else:
            return False
