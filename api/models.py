from django.db import models


# Create your models here.


class Student(models.Model):
    FROM = models.EmailField(max_length=200,null=False)
    NAME = models.CharField(max_length=200,null=False)
    SUPJECT = models.CharField(max_length=200,null=False)
    PHONE = models.IntegerField(null=False)
    CONTEXT = models.TextField(null=False)

