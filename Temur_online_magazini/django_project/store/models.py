from django.db import models
from django.contrib.auth.models import User
from teritories.models import *


class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    # address=models.ForeignKey(Territorie, on_delete=models.CASCADE, default='Olmazor')
    address=models.CharField(max_length=200, null=True)
    territoie=models.ForeignKey(Territorie,on_delete=models.SET_NULL)
    def __str__(self):
        return self.user.__str__()

    @property
    def full_name(self):
        return self.user.first_name+' '+ self.user.last_name
class Categories(models.Model):
    category_name=models.CharField(max_length=200, null=False)
    describtion= models.CharField(max_length=300, null=True)
    def __str__(self):
        return self.category_name

class Products(models.Model):
    category=models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=200, null=False)
    price= models.FloatField(null=False)
    image=models.ImageField(null=True)
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
    def __str__(self):
        return self.product_name
class Orders(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    order_date=models.DateTimeField(auto_now_add=type)
    status= models.CharField(default='start', max_length=10)
    delivered_date=models.DateTimeField(null=True)
    def __str__(self):
        return str(self.id)+ self.status
class Order_details(models.Model):
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    order=models.ForeignKey(Orders, on_delete=models.CASCADE)
    quantity= models.IntegerField(default=0, null=True)
    @property
    def total(self):
        return self.quantity * self.product.price
    def add(self,quantity=1):
        self.quantity+=1
        self.save()
    def sub(self,quantity=1):
        if self.quantity-quantity>0:
            self.quantity -= quantity
            self.save()
        else:
            self.delete()
    def action(self,data):
        if data['action']=='add':
            self.add(data['quantity'])
        else:
            self.sub()


