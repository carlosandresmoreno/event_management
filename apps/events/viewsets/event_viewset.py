from rest_framework import viewsets
from apps.events.models import Event
from apps.events.serializers.event_serializer import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    model = Event
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    # http_method_names = ["get", "post"]
