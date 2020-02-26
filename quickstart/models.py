# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employee(models.Model):
    employeeid = models.IntegerField()
    employeename = models.CharField(max_length=100)
    squadname = models.CharField(max_length=25)
    project = models.CharField(max_length=25)


class Task(models.Model):
    employeename = models.CharField(max_length=100)
    jiraid = models.IntegerField()
