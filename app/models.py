from email.policy import default
from importlib.resources import contents
from statistics import mode
from django.db import models
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.




class Blog(models.Model):
    title_uz = models.CharField(max_length=300, default="")
    title_ru = models.CharField(max_length=300, default="")
    title_en = models.CharField(max_length=300, default="")
    subtitle_uz = models.TextField(default="", blank=True, null=True)
    subtitle_ru = models.TextField(default="", blank=True, null=True)
    subtitle_en = models.TextField(default="", blank=True, null=True)
    body_uz = HTMLField(default="")
    body_ru = HTMLField(default="")
    body_en = HTMLField(default="")
    blog_image = models.ImageField(upload_to="static/blog_images/")
    slug = models.CharField(max_length=300, blank=True)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title_uz


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_uz)
        return super().save(*args, **kwargs)



class School(models.Model):
    title = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    rating = models.FloatField()
    image = models.ImageField(upload_to="static/schools_img/", default="a.png")


    def __str__(self):
        return self.title


class Members(models.Model):
    fullname = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    image = models.ImageField(upload_to="static/members/", default="member.png")


    def __str__(self):
        return self.fullname





