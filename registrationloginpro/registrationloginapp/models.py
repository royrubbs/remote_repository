from django.db import models

class RegistrationData(models.Model):
    name = models.CharField(max_length=20)
    password1 = models.CharField(max_length=30,blank=False)
    email = models.EmailField(max_length=50,blank=False)
    mobile = models.BigIntegerField()


