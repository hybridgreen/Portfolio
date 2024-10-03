from django.db import models
from django.utils import timezone

# Create your models here.

class Notes(models.Model):
    PRIORITY_CHOICES = [
        ("1", "Low"),
        ("2" , "Medium"),
        ("3", "High")
    ]
    
    title = models.CharField(max_length=100)
    content = models.CharField (max_length=1000)
    date = models.DateTimeField (default=timezone.now)
    priority_level = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default = "3")

    def __str__(self):
        return self.title