from django.db import models

# Create your models here.
from django.urls import reverse

class Employee(models.Model):
    name = models.CharField(max_length=200)
    employee_id = models.IntegerField()
    email = models.EmailField(max_length=80)


    def __str__(self):
        return self.name