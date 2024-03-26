from django.db import models
# Create your models here.
#habits users want to track
class Habit(models.Model):
    HABIT_TYPE_CHOICES = (
        ('integer', 'Integer'),
        ('yes_no', 'Yes/No'),
        ('timer', 'Timer'),
    )  
    name = models.CharField(max_length=100)
    description = models.TextField()
    frequency = models.CharField(max_length=20)  # e.g., daily, weekly
    start_date = models.DateField()
    habit_type = models.CharField(max_length=10, choices=HABIT_TYPE_CHOICES, default = 'yes_no')
    
    def __str__(self):
      return (f"{self.name}-{self.description}-{self.frequency}-{self.start_date}-{self.habit_type}")

    
