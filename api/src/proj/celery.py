from celery import Celery

app = Celery('proj', broker='redis://redis:6379/0', backend='redis://redis:6379/0', include=["proj.tasks"])
