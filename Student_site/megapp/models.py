from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Member(models.Model):
    Firstname = models.CharField(max_length=500)
    Lastname = models.CharField(max_length=500)
    course = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    college = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    sign_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.Firstname)


class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.search)
    class Meta:
        verbose_name_plural = 'searches'
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    course = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username

