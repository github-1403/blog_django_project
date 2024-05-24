from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def post_list_view(request):
    posts_list = Post.objects.all()
    context = {'all_posts': posts_list}
    return render(request, template_name='blog/posts_list.html', context=context)


