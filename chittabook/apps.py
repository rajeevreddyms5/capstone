from django.apps import AppConfig
from .management.commands import apply_default_categories


class ChittabookConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "chittabook"

    # save the profile instance when user is created
    def ready(self):
        import chittabook.signals


        self.management_commands = {
            'apply_default_categories': apply_default_categories.Command,
        }