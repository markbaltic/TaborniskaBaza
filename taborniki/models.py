# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.db import models



# Create your models here.

class Clan(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


    def __str__(self):
        return self.first_name

