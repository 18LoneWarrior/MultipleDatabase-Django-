from django.db import models

# Create your models here.


class Result(models.Model):
    subject = models.CharField(max_length=100)
    score = models.IntegerField()
    max_score = models.IntegerField()
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.subject} {self.score} {self.max_score}"
