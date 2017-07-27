from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    """
    Published blog posts sorted by published_date
    """
    posts = Post.objects.filter(published_date__lt=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    """
    Publish the details of the post on a separate link.
    """
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})