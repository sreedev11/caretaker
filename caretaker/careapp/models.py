from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse





class Category(models.Model):
    name = models.CharField(max_length=255,null=True)
    


class Surgicals(models.Model):
    group = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='category_images/', null=True)

    def get_delete_url(self):
        return reverse('delete_surgical', args=[str(self.id)])
    

class AdminProfile(models.Model):
    profile_picture = models.ImageField(upload_to='admin_profiles/')
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
