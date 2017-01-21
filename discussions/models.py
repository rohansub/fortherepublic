from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
class Politician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    rep_location = models.CharField(max_length=100)
    num_issues = models.IntegerField(default=0)

class Issue(models.Model):
    points = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    politician = models.ForeignKey(Politician, on_delete=models.CASCADE)
