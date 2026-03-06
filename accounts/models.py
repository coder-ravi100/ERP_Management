from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
class User(AbstractUser):
    role = models.ForeignKey(Role,on_delete = models.SET_NULL, null = True, blank = True)

    def __str__(self):
        return f"{self.username}" 
    
