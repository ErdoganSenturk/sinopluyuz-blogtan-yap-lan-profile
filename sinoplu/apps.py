from django.apps import AppConfig


class SinopluConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sinoplu'

    def ready(self):
        import sinoplu.signals

