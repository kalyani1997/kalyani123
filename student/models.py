from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    mob=models.BigIntegerField()
    rollno=models.IntegerField()
    fees=models.FloatField()

