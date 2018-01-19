# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class House(models.Model):
	name = models.CharField(max_length=255)

class Student(models.Model):
	name = models.CharField(max_length=255)
	house = models.ForeignKey(House, related_name="students")