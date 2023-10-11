from django.db import models

# Create your models here.

class Project(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    link=models.CharField(max_length=500)
    description=models.TextField()