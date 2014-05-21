from rest_framework import viewsets

from .models import Activity, TimeEntry


class ActivityViewSet(viewsets.ModelViewSet):
    model = Activity


class TimeEntryViewSet(viewsets.ModelViewSet):
    model = TimeEntry
