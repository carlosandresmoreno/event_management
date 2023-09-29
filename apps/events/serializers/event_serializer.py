from rest_framework import serializers
from apps.events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["event_type", "description", "date", "status"]
