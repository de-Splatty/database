from django.db import models

# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    names = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
    password = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, default="Male")
    dob = models.DateField(null=True, blank=True) # default

    class Meta:
        db_table = 'customers'



