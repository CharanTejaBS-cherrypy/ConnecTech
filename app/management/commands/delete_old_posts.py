# myapp/management/commands/delete_old_posts.py
from django.core.management.base import BaseCommand
from app.models import Post


class Command(BaseCommand):
    help = 'Delete old posts'

    def handle(self, *args, **kwargs):
        Post.delete_old_posts()
        self.stdout.write(self.style.SUCCESS('Successfully deleted old posts'))
