# models.py

from django.db import models
from django.contrib.auth.models import User


class Hackathon(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='okay')
    rules = models.TextField(default='okay')
    teams = models.IntegerField(default=1)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Team(models.Model):
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField(Participant)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
