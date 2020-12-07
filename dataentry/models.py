from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
 
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    family_members = models.CharField(max_length=50)
    dob = models.DateField()
    doa = models.DateField()
    created_ts = models.DateField(default=datetime.date.today, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name