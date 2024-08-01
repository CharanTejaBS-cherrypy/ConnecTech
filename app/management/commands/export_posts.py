# myapp/management/commands/export_posts.py
from django.core.management.base import BaseCommand
from app.utils import export_posts_to_excel


class Command(BaseCommand):
    help = 'Export posts to Excel'

    def handle(self, *args, **kwargs):
        export_posts_to_excel()
        self.stdout.write(self.style.SUCCESS(
            'Successfully exported posts to Excel'))
