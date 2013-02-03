from django.db import models
from django.contrib.auth.models import User

class Manager(User):
    # username
    # password
    # email
    # first_name
    # last_name
    pass
    
class Team(models.Model):
    manager = models.ForeignKey(Manager)
    name = models.CharField(max_length=64)
    
class Dev(models.Model):
    teams = models.ManyToManyField(Team)
    login = models.CharField(max_length=64, primary_key=True)
    avatar_url = models.CharField(max_length=256)
    email = models.EmailField()
    
class Commit(models.Model):
    dev = models.ForeignKey(Dev)
    time = models.TimeField()
    sha = models.CharField(max_length=40)
    
class GitCache(models.Model):
    dev = models.ForeignKey(Dev)
    last_updated = models.TimeField(auto_now = True)
    
