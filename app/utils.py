# myapp/utils.py
from openpyxl import Workbook
from app.models import Post
from django.utils import timezone
from datetime import timedelta


def export_posts_to_excel():
    three_days_ago = timezone.now() - timedelta(days=3)
    old_posts = Post.objects.filter(created_at__lt=three_days_ago)

    # Create a new Excel workbook
    wb = Workbook()
    ws = wb.active

    # Write header row
    ws.append(['User', 'Image URL', 'Description', 'Created At', 'Likes'])

    # Write post data to Excel rows
    for post in old_posts:
        likes = ', '.join([user.username for user in post.likes.all()])
        ws.append([post.user.username, post.image.url,
                  post.description, post.created_at, likes])

    # Save the workbook
    wb.save('old_posts.xlsx')
