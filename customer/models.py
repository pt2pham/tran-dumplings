from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(
        max_length=100
    )
    last_Name = models.CharField(
        max_length=100
    )
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_Name