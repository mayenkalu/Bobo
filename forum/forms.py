from django import forms
from .models import Thread, Post, Comment

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'category']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']