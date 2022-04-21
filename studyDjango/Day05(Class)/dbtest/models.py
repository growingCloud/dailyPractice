from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    subject = models.TextField()

    def __str__(self):
        return self.name + "선생님"