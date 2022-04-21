from django.db import models


# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    likey = models.IntegerField()

    def __str__(self):
        return self.subject

    def summary(self):
        return self.content[:150] + "..."

    def hot(self):
        if self.likey > 20:
            return True
        return False
