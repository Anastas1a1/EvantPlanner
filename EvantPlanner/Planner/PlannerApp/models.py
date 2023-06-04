from django.db import models


class Organization(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)

class UserProfile(models.Model):
    username = models.CharField(max_length=128, default='User')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    organization = models.ManyToManyField(Organization, default='Нет организации')
    

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    organizations = models.ManyToManyField(Organization)
    image = models.ImageField(upload_to='event_images')
    date = models.DateTimeField()