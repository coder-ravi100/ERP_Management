from django.db import models
from accounts.models import User

# Create your models here.
class Leave(models.Model):

    STATUS_CHOICES = [
        ('Pending','Pending'),
        ('Approved','Approved'),
        ('Rejected','Rejected'),
    ]

    employee = models.ForeignKey(User,on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='Pending')

    approved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_leaves'
    )

    def __str__(self):
        return f"{self.employee} - {self.status}"