from django.db import models

# Create your models here.

class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name