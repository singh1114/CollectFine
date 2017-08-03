# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class GdMoney(models.Model):
    name = models.CharField(max_length=200)
    fine = models.IntegerField()
    money_earned = models.IntegerField()
    paid = models.IntegerField()
