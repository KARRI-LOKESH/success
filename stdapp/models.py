from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    rollno=models.CharField(max_length=10)
    age=models.IntegerField()
    email=models.EmailField(max_length=25)
    phone = models.IntegerField(null=True)