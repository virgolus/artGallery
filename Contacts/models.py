from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telephone = models.IntegerField()
    location =  models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    cap = models.IntegerField()
    birthDate = models.DateField()    
    # method
    #def was_published_today(self):
    #    return self.pub_date.date() == datetime.date.today()
    #description
    #was_published_today.short_description = 'Published today?'

    # toString
    def __unicode__(self):
        return self.name + "-" + self.surname  