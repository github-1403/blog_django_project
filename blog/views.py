from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list_view(request):
    posts_list = Post.objects.all()
    context = {'all_posts': posts_list}
    return render(request, template_name='blog/posts_list.html', context=context)


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    return render(request, template_name='blog/post_detail.html', context=context)

