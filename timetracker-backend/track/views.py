from rest_framework import viewsets

from .models import Activity, TimeEntry
from .serializers import TimeEntrySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    model = Activity


class TimeEntryViewSet(viewsets.ModelViewSet):
    model = TimeEntry
    serializer_class = TimeEntrySerializer

    def get_queryset(self):
        return self.request.user.entries.all()

    def pre_save(self, obj):
        obj.user = self.request.user
