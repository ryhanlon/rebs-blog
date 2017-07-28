from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm


def post_list(request):
    """
    Published blog posts sorted by published_date
    """
    posts = Post.objects.filter(published_date__lt=timezone.now()).order_by('published_date')
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    """
    Publish the details of the post on a separate link.
    """
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)


def post_new(request):
    """
    Publish the interface to add a new blog post.
    """
    form = PostForm()
    context = {'form': form}
    return render(request, 'blog/post_edit.html', context)
