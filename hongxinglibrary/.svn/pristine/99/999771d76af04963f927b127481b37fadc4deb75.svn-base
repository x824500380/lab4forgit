from django.db import models
from django.contrib import admin

# Create your models here.
class Author(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=100,blank = True)
    AuthorID = models.CharField(primary_key=True,max_length=100)
    Country = models.CharField(max_length=100,blank = True)

    def __unicode__(self):
        return u'%s'%self.AuthorID
 
class Book(models.Model):
    Publishdate = models.CharField(max_length=100,blank = True)
    ISBN = models.CharField(primary_key=True,max_length=13)
    Title = models.CharField(max_length=100)
    Price = models.FloatField(max_length=100,blank = True)
    Publisher = models.CharField(max_length=200,blank = True)
    AuthorID = models.ForeignKey(Author)

    def __unicode__(self):
        return u'%s'%self.AuthorID