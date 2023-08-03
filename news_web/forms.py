from django import forms

from news_api.models import Post, Comment


class PostInput(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "link"]


class CommentInput(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
