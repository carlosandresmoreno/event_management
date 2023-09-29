from django.db.models.signals import pre_save, post_save, post_migrate
from django.dispatch import receiver
from .models import Event, EventStatus, EventType
from datetime import datetime

@receiver(pre_save, sender=Event)
@receiver(post_save, sender=Event)  
def update_requires_management(sender, instance, **kwargs):
    if instance.status.name == "Revisado":  
        instance.requires_management = True
    else:
        instance.requires_management = False
    

@receiver(post_migrate)
def initialize_data(sender, **kwargs):
    if not EventType.objects.exists() or not EventStatus.objects.exists() or not Event.objects.exists():
        event_type_1, _ = EventType.objects.get_or_create(name="Evento tipo 1")
        event_type_2, _ = EventType.objects.get_or_create(name="Evento tipo 2")
        event_type_3, _ = EventType.objects.get_or_create(name="Evento tipo 3")
        event_status_pendiente, _ = EventStatus.objects.get_or_create(name="Pendiente")
        event_status_revisado, _ = EventStatus.objects.get_or_create(name="Revisado")
        
        example_event_1 = Event(
            event_type=event_type_1,
            description="Descripción del evento 1",
            date=datetime.now(),
            status=event_status_pendiente,
            requires_management=True
        )
        example_event_1.save()

        example_event_2 = Event(
            event_type=event_type_2,
            description="Descripción del evento 2",
            date=datetime.now(),
            status=event_status_revisado,
            requires_management=False
        )
        example_event_2.save()

        example_event_3 = Event(
            event_type=event_type_3,
            description="Descripción del tercer objeto",
            date=datetime.now(),
            status=event_status_revisado,
            requires_management=False
        )
        example_event_3.save()