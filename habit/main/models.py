from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#habits users want to track
class Habit(models.Model):
    
    HABIT_FREQUENCY_CHOICES = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    name = models.CharField(max_length=100)
    
    category = models.TextField(default= "")
    
    description = models.TextField()
    
    frequency = models.CharField(max_length=20, choices=HABIT_FREQUENCY_CHOICES)
    
    start_date = models.DateField()
    
    completed = models.BooleanField(default=False) 
    
    
    def __str__(self):
      return (f"{self.name}-{self.category}-{self.description}-{self.frequency}-{self.start_date}-{self.completed}")
 