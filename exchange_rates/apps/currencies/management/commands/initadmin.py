from django.contrib.auth.models import User
from django.core.management import BaseCommand

from core import settings


class Command(BaseCommand):
    help = 'Создает админа (root:root)'
    def handle(self, *args, **options):
        if not User.objects.filter(is_superuser=True):
            admin = User.objects.create_superuser(
                username='root',
                password='root',
            )
            admin.is_superuser = True
            admin.save()
        self.stdout.write(self.style.SUCCESS("Админ создан!"))