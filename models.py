from django.db import models

# Create your models here.


class Customer(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    number=models.BigIntegerField()
    city=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

    class Meta:
        db_table="customer_details"


class Blog(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    image=models.ImageField( blank=True, default='No Image')
    audio=models.FileField(blank=True, default=' No Audio')
    video=models.FileField( blank=True, default='No Video')
    class Meta:
        db_table="Blog"


class Admin(models.Model):
    admin=models.CharField(max_length=100)
    password=models.CharField(max_length=100)