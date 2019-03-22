from django.db import models

# Create your models here.
class BikeSale(models.Model):
    ServiceName=models.CharField(max_length=45)
    Description=models.CharField(max_length=150)

class BikePurchase(models.Model):
    ServiceName=models.CharField(max_length=45)
    Description=models.CharField(max_length=150)

class PostEnquiry(models.Model):
    Name=models.CharField(max_length=40)
    Vehicle=models.CharField(max_length=40)
    BIKE_Model=models.CharField(max_length=35)
    Color=models.CharField(max_length=35)
    Contact_Number=models.CharField(max_length=15)
