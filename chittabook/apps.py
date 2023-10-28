from django.apps import AppConfig


class ChittabookConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "chittabook"

    # save the profile instance when user is created
    def ready(self):
        import chittabook.signals