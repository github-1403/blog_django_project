from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from .forms import NewPostForm
from django.shortcuts import redirect, reverse


def post_list_view(request):
    posts_list = Post.objects.filter(status="pub")
    context = {'all_posts': posts_list}
    return render(request, template_name='blog/posts_list.html', context=context)


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    return render(request, template_name='blog/post_detail.html', context=context)


def post_create_view(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to=reverse('posts_list'))
    else:
        form = NewPostForm()

    return render(request, 'blog/post_create.html', context={'form': form})

