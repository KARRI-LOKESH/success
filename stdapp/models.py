from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    rollno = models.CharField(max_length=10, unique=True)
    age = models.IntegerField()
    email = models.EmailField(max_length=25)
    phone = models.IntegerField(null=True)

    class Meta:
        unique_together = ('rollno', 'email')

    def __str__(self):
        return f"{self.name} ({self.rollno})"
