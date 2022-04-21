from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    comment = models.TextField()

class Test(models.Model):
    num = models.IntegerField(primary_key=True)