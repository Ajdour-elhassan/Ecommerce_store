from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User


class Services(models.Model) :
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to="images")


    class Meta :
        ordering = ("name",)
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def __str__(self) :
        return self.name 

class Works(models.Model) :
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to="images")


    def __str__(self) :
        return self.name 
    
    class Meta :
        ordering = ('name',)
        verbose_name = 'work'
        verbose_name_plural = 'works'


class Teams(models.Model) :
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to="images")
    description = models.CharField(max_length=400)

    class Meta : 
        ordring : ('name',)
        verbose_name = 'team'
        verbose_name_plural = 'teams'

    def __str__(self) :
        return self.name


class Feedback(models.Model) :
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to="images")
    description = models.CharField(max_length=400)

    class Meta : 
        ordring : ('name',)
        verbose_name = 'feedback'
        verbose_name_plural = 'feedbacks'

    def __str__(self) :
        return self.name

class Contact(models.Model) :
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self) :
        return self.name 

    



        

        
        
    
    