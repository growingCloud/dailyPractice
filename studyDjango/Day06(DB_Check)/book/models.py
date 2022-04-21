from django.db import models

# Create your models here.
class Book(models.Model):
    site_name = models.CharField(max_length=100)
    site_url = models.TextField()

    def __str__(self):
        return self.site_name