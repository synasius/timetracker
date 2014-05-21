from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class TimeEntry(models.Model):
    activity = models.ForeignKey(Activity)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "Entry for {}".format(self.activity)
