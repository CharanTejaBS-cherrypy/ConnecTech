from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class Community(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    logo_url = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content[:20]}'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def total_likes(self):
        return self.likes.count()

    @classmethod
    def delete_old_posts(cls):
        three_days_ago = timezone.now() - timedelta(days=3)
        old_posts = cls.objects.filter(created_at__lt=three_days_ago)
        old_posts.delete()


class Reaction(models.Model):
    post = models.ForeignKey(
        Post, related_name='reactions', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reaction_type = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


class Idea(models.Model):
    title = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.title


