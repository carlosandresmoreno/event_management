from django.db import models
from django_extensions.db.models import TimeStampedModel


class EventType(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class EventStatus(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Event(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    event_type = models.ForeignKey(EventType, on_delete=models.PROTECT)
    description = models.TextField(default="", blank=False, null=False)
    date = models.DateTimeField()
    status = models.ForeignKey(EventStatus, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.event_type} - {self.description}"

    class Meta:
        verbose_name_plural = "Events"
