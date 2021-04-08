from django.db import models


# # Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    email= models.CharField(max_length=50)
    phone=models.CharField(max_length=15)

    def __str__(self):
        return "Name :" + self.name  + " - Email is :" + self.email
    