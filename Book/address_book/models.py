from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
