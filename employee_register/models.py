# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# Create your models here.
class Employee(models.Model):
    fullName = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

