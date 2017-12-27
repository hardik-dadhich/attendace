from django.db import models


# Create your models here.
class Sign_details(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    shift = models.CharField(max_length=20)
    mob_no = models.CharField(max_length=10)
    Password = models.CharField(max_length=20)
    confrom_pass = models.CharField(max_length=20)


class Login(models.Model):
    name = models.ForeignKey(Sign_details, on_delete=models.CASCADE)
    password = models.CharField(max_length=20)