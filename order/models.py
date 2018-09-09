from django.db import models
from customer.models import Customer

# Create your models here.

class Order(models.Model):
    first_name           = models.CharField(max_length=100, null=True, blank=False)
    last_name            = models.CharField(max_length=100, null=True, blank=False)
    email                = models.EmailField(max_length=100, null=True, blank=True)
    dumpling_type        = models.CharField(max_length=10, null=True, blank=False)
    quantity             = models.IntegerField(blank=False)
    special_instructions = models.TextField(max_length=200, null=True, blank=True)
    timestamp            = models.DateTimeField(auto_now_add=True, null=True)
