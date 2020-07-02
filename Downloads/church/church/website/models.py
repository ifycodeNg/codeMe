from django.db import models
from ckeditor.fields import RichTextField
class Post(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField()
    Images=models.ImageField(null=True,blank=True,upload_to="images/")
    description=RichTextField(blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Events(models.Model):
    pass;

class Sermon(models.Model):
    pass;
class Message(models.Model):
    fullname=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    dateTime=models.DateTimeField(auto_now_add=True)
    message=models.TextField()
    phone_number=models.IntegerField()

    def __str__(self):
        return self.fullname;



    