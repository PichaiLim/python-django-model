from django.db import models
# from django.db.models import Model

# Create your models here.
class PostModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    active = models.BooleanField(default=True) #empty in the database
    title = models.CharField(max_length=240, verbose_name='Post title') # 'verbose_name' => change label name
    content =  models.TextField(null=True, blank=True)
    pass
    class Metal:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'



""" 
python manage.py makemigrations # every time you change models.py
python manage.py migate
"""