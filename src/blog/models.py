from django.db import models
# from django.db.models import Model

# Create your models here.
class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    active = models.BooleanField(default=True) #empty in the database
    title = models.CharField(max_length=240)
    content =  models.TextField(null=True, blank=True)
    pass



""" 
python manage.py makemigrations # every time you change models.py
python manage.py migate
"""