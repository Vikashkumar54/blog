from django.db import models

# Create your models here.
 


class signform(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    confirm=models.CharField(max_length=255)
    
from cloudinary.models import CloudinaryField
class add(models.Model):
    title=models.CharField(max_length=255)
    image=CloudinaryField('image')
    description=models.TextField()
    descrip=models.CharField(max_length=255)
    created_by=models.CharField(max_length=222)

class contactu(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    number=models.IntegerField()
    address=models.TextField()
    
class proimage(models.Model):
    image=CloudinaryField('image')
    user = models.CharField(max_length=255)



