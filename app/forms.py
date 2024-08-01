from django import forms
from .models import Post, Idea


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description']


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'domain', 'description', 'email']



