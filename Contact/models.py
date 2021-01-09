from django.db import models
from django.contrib.auth.models import User


class ContactDetails(models.Model):
    firstname = models.CharField(verbose_name="Firstname", max_length=100)
    lastname = models.CharField(verbose_name="Lastname", max_length=100)
    email = models.EmailField(verbose_name="Email", max_length=100, unique=True)
    phone = models.CharField(verbose_name="Mobile Phone", max_length=12, unique=True)
    address = models.CharField(max_length=100)
    user_id = models.ForeignKey(User)

    def __unicode__(self):
        return u"%s %s" % (self.firstname, self.lastname)

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)