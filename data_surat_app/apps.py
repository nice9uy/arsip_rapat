from django.apps import AppConfig


def create_group(sender, **kwargs):
    from django.contrib.auth.models import Group

    group_names = [
        "super_admin",
        "admin",
    ]

    # Check if the group already exists to avoid duplicates
    for group_name in group_names:
        if not Group.objects.filter(name=group_name).exists():
            Group.objects.create(name=group_name)

class DataSuratAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'data_surat_app'

    def ready(self):
        # import surat_masuk.signals
        from django.db.models.signals import post_migrate
        post_migrate.connect(create_group, sender=self)