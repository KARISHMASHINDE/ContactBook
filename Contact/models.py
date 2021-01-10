from django.db import models
from django.contrib.auth.models import User


class ContactDetails(models.Model):
    firstname = models.CharField( max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField( max_length=12, unique=True)
    address = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s %s" % (self.firstname, self.lastname)

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)
    
