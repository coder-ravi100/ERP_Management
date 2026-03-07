from django.db import models
from accounts.models import User
from departments.models import Department

# Create your models here.
class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    designation = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    salary = models.IntegerField()
    join_date = models.DateField()
    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="managed_employees"
    )

    def __str__(self):
        return str(self.user)