from django.db import models
from accounts.models import User
from departments.models import Department

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    employee = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee} - {self.team}"
    