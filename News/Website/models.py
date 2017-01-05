from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.


#Firstly we need to build Query manager:

class NewsManager(models.Manager):

    def query_by_Author(self,Author_id):
        query=self.get_queryset().filter(Author_id=Author_id)
        return query

    def query_by_Tag(self,Tag_id):
        query=self.get_queryset().filter(Tag_id=Tags_id)
        return query

    def query_by_time(self):
        query=self.get_queryset().order_by('Modify_Time')
        return query

    def query_by_keyword(self,keyword):
       query=self.get_queryset().filter(title__contains=keyword)

class CommentManager(models.Manager):

    def query_by_time(self):
        quert=self.get_queryset().order_by('-Create_Date')



#Now, we create the data models base on Website Design:

class News(models.Model):

    objects=NewsManager()

    Title=models.CharField('Title',max_length=40)
    Content=models.TextField('Content',max_length=1000)  #Need to set the width
    Create_Time=models.DateField('Create_Time',auto_now_add=True)
    Modify_Time=models.DateField('Modify_Time') #Try do not use auto_now_add
    Tags=models.ManyToManyField('Tags',verbose_name='Tags')
 
class Tags(models.Model):
    Group=models.CharField('Group',max_length=40)

class Author(models.Model):
    Name=models.CharField('Name',max_length=40)
    Profile=models.TextField('Profile',max_length=256)
    News=models.ForeignKey(News,verbose_name='News',null=True,default='None')

class Users(AbstractUser):
    Name=models.CharField('Name',max_length=40)
    Birth=models.DateField('Birth',null=True,editable=True)
    Profile=models.TextField('Profile',max_length=256,default='No profile')
    Create_Date=models.DateField('Create_Date',auto_now_add=True)

class Comments(models.Model):

    objects=CommentManager()

    Name=models.CharField('Name',max_length=40)
    Email=models.EmailField('Email')
    Comment=models.TextField('Comment',max_length=256,default='Comment')
    Create_Date=models.DateField('Create_Date',auto_now_add=True)
    News=models.ForeignKey('News',verbose_name='News',null=True)

