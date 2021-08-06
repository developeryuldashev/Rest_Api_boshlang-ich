from django.db import models
from django.contrib.auth.models import User
from teritories.models import *
class Employee(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=20,null=True)
    image=models.ImageField(null=True)
    adress=models.CharField(max_length=200,null=True)
    territorie=models.ManyToManyField(Territorie,on_delete=models.SET_NULL)
    @property
    def full_name(self):
        return self.user.first_name+' '+ self.user.last_name



# Create your models here.
