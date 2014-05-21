from __future__ import unicode_literals
from rest_framework import serializers

from .models import TimeEntry


class TimeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeEntry
        read_only_fields = ("user",)
