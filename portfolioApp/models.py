from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from colorfield.fields import ColorField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.


class Patient(models.Model):
    Dentist=models.ForeignKey(User,on_delete=models.CASCADE)
    PatientName=models.CharField(max_length=100)
    PatientID=models.CharField(max_length=30)
    Clinic=models.CharField(max_length=300)
    Prescriber=models.CharField(max_length=200)
    Invoice=models.CharField(max_length=20)
    Balance_To_Pay=models.CharField(max_length=30)
    Surgery=models.CharField(max_length=100)
    Fee=models.CharField(max_length=30)
    Status=models.CharField(max_length=100)
    Note=models.TextField()
    Date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.PatientID + "  |  " + self.PatientName + "  |  " + str(self.Date) 
    
# class Post(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
#     Title=models.CharField(max_length=150)
#     slug = models.SlugField(unique=True,null=True,blank=True)
#     Meta_Tags = models.CharField(max_length=200,)
#     Description=models.TextField()
#     Category=models.CharField(max_length=50)
#     Body=RichTextUploadingField()
#     Date=models.DateField(auto_now_add=True)   
#     Views=models.IntegerField(default=0,null=True)
#     Likes=models.IntegerField(default=0,null=True)
#     Dis_Likes=models.IntegerField(default=0,null=True)
#     CommentsCounts=models.IntegerField(default=0,null=True)
#     def __str__(self):
#         return self.Title + " | " + str(self.Date)

# def createslug(instance,new_slug=None):
#     slug=slugify(instance.Title)
#     if new_slug is not None:
#         slug=new_slug
#     qs = Post.objects.filter(slug=slug).order_by("-id")
#     exists=qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug,qs.first().id)
#         return createslug(instance,new_slug=new_slug)
#     return slug
# def pre_save_post_receiver(sender,instance,*args, **kwargs):
#     if not instance.slug:
#         instance.slug=createslug(instance)
# pre_save.connect(pre_save_post_receiver,Post)

# class Comment(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE)
#     Post=models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
#     Body=models.TextField(null=True)
#     Time=models.DateTimeField(auto_now_add=True,null=True)
#     def __str__(self):
#         return str(self.Post) + " | "  + self.Body + " | " + self.user.username + " | " + str(self.Time)        
