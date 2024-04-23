from celery import shared_task
from datetime import date, timedelta
from .models import Habit

@shared_task
def update_habit_completion_statuses():
    habits = Habit.objects.all()

    for habit in habits:
        if habit.frequency == 'daily':
            
            habit.completed = False
            habit.save()
        elif habit.frequency == 'weekly':
            
            if date.today().weekday() == 6:  
                habit.completed = False
                habit.save()
        elif habit.frequency == 'monthly':
            
            if date.today().day == 1:  
                habit.completed = False
                habit.save()
