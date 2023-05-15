from django.db import models
from ckeditor.fields import RichTextField 

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
    description=RichTextField()
    created_by=models.CharField(max_length=222)
    Permission=models.BooleanField(default=False)

class contactu(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    number=models.IntegerField()
    address=models.TextField()
    
class feedback(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    number=models.IntegerField()
    message=models.TextField()
    
class proimage(models.Model):
    image=CloudinaryField('image')
    user = models.CharField(max_length=255)
    
class leavecomment(models.Model):
    adds_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    comment = models.CharField(max_length=400)
    
    def __str__(self) -> str:
        return self.adds_id



