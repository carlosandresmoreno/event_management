from django.apps import AppConfig


class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.events'

    # Agrega esta línea de importación
    def ready(self):
        import apps.events.signals
