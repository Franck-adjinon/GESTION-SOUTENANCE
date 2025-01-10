from django.apps import AppConfig


class SoutappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'soutapp'
    
    def ready(self):
        import soutapp.signals  # Importer le fichier signals.py