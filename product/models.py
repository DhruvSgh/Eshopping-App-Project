from django.db import models
from django.contrib.auth.models import User,auth

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    cat=models.CharField(max_length=50)
    cmp=models.CharField(max_length=50)
    pimg=models.ImageField(upload_to="pic")

    def __str__(self):
        return self.name

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    address=models.TextField()
    mobile=models.CharField(max_length=50)
    def __str__(self):
        return self.user.username