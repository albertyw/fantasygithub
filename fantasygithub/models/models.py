from django.db import models
from django.contrib.auth.models import User

#class Manager(User):
#    username
#    password
#    email
#    first_name
#    last_name
#    pass
#    class Meta:
#        app_label = 'fantasygithub'

class Team(models.Model):
    manager = models.ForeignKey(User)
    name = models.CharField(max_length=64)
    class Meta:
        app_label = 'fantasygithub'

class Dev(models.Model):
    teams = models.ManyToManyField(Team)
    login = models.CharField(max_length=64, primary_key=True)
    avatar_url = models.CharField(max_length=256)
    last_updated = models.DateTimeField(auto_now = True)
    class Meta:
        app_label = 'fantasygithub'

class Commit(models.Model):
    dev = models.ForeignKey(Dev)
    time = models.DateTimeField()
    sha = models.CharField(max_length=40)
    class Meta:
        app_label = 'fantasygithub'
