from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'habit.settings')

app = Celery('habit')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

from celery.schedules import crontab

app.conf.beat_schedule = {
    'update-habit-completion-statuses': {
        'task': 'app.tasks.update_habit_completion_statuses',
        'schedule': crontab(minute=0, hour=0),  # Run daily at midnight
    },
}
