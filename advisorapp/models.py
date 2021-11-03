from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class users(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.name

class addadvisor(models.Model):
    advname=models.CharField(max_length=200,null=True)
    profilepic = models.ImageField(null=True,blank=True,upload_to='images/')
    objects = models.Manager()

    def __str__(self):
        return str(self.advname)

class advdisplay(models.Model):
    advname=models.ForeignKey(addadvisor,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    objects = models.Manager()
    def __str__(self):
        return str(self.advname)

class Bookadvisor1(models.Model):
    advname = models.ForeignKey(addadvisor,blank=True, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.advname)

class db(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    passord=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class info(models.Model):
    infoname = models.ForeignKey(addadvisor,null=True,on_delete=models.CASCADE)
    datecreated = models.DateTimeField(auto_now_add=True,null=True)
    name = models.CharField(max_length=200,null=True)
