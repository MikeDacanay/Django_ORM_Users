# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "first name should be more than 5 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "last desc should be more than 10 characters"
        return errors;

class Users(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email= models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True) 
	updated_at = models.DateTimeField(auto_now = True)
	objects = UsersManager()