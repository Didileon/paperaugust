import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
#app.conf.beat_schedule = {
 #   'action_every_30_sec': {
  #      'task': 'news.tasks.text',
   #     'schedule': 30,
    #    'args': (),
    #},
#}

#app.conf.beat_schedule = {
 #   'action_every_30_sec': {
  #      'task': 'news.tasks.my_job',
   #     'schedule': 30, #crontab(hour=8, minute=0, day_of_week=1),
    #    'args': (),
    #},
#}



app.conf.beat_schedule = {
    'action_every_35_sec': {
        'task': 'news.tasks.text',
        'schedule': 30.00,
        'args': (),
    },
    'action_every_monday_morning': {
        'task': 'news.tasks.my_job',
        'schedule': crontab(hour=8, minute=0, day_of_week=1),
        'args': (),
    }
}