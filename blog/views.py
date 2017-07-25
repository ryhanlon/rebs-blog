from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    """
    Published blog posts sorted by published_date
    """
    posts = Post.objects.filter(published_date__lt=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
