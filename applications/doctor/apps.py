from django.apps import AppConfig


class DoctorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.doctor'

    def ready(self):
        import applications.doctor.signals
