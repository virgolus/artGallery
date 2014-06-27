from django.db import models

# Create your models here.
import datetime

class Contact(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telephonel = models.IntegerField
    pub_date = models.DateTimeField('date published')
    # method
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    #description
    was_published_today.short_description = 'Published today?'
    # toString
    def __unicode__(self):
        return self.surname + "-" + self.name 
