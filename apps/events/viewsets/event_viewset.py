from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.events.models import Event
from apps.events.serializers.event_serializer import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    @action(detail=True, methods=["get"])
    def requires_management(self, request, pk=None):
        """
        Gets events that do or do not require handling. receives 1 or 2 as parameter
        """
        if pk not in ["0", "1"]:
            return Response({"error": "The value should be '0' or '1'"}, status=status.HTTP_400_BAD_REQUEST)
        
        event_type_names = ["Evento tipo 1"] if pk == "1" else ["Evento tipo 3"]
        requires_management = Event.objects.filter(requires_management=True, event_type__name__in=event_type_names)
        if requires_management.exists():
            return Response(EventSerializer(requires_management, many=True).data)
        else:
            return Response({"message": "No events found for the specified option."}, status=status.HTTP_404_NOT_FOUND)
