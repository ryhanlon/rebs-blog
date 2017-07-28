from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    """
    Interface to edit blog posts.
    """

    class Meta:
        model = Post
        fields = ('title', 'text',)