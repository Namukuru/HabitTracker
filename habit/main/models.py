from django.db import models
# Create your models here.
#habits users want to track
class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    frequency = models.CharField(max_length=20)  # e.g., daily, weekly
    start_date = models.DateField()
    def __str__(self):
      return self.name

    
