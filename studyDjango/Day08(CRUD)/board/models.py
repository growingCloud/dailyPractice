from django.db import models


# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.subject

class Reply(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    replyer = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return f"{self.board}_{self.replyer}"