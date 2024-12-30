from django.db import models

# Create your models here.
class student(models.Model):
    name=models.TextField()
    age=models.IntegerField()
    email=models.TextField()

    def __str__(self):
        return self.name