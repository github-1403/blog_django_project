from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from .forms import NewPostForm
from django.shortcuts import redirect, reverse
from django.views import generic


# def post_list_view(request):
#     posts_list = Post.objects.filter(status="pub").order_by('-datetime_modified')
#     context = {'all_posts': posts_list}
#     return render(request, template_name='blog/posts_list.html', context=context)
#

class PostListView(generic.ListView):
    context_object_name = "all_posts"
    template_name = "blog/posts_list.html"

    def get_queryset(self):
        return Post.objects.filter(status="pub").order_by('datetime_modified')


# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     context = {"post": post}
#     return render(request, template_name='blog/post_detail.html', context=context)
#

class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"


# def post_create_view(request):
#     if request.method == "POST":
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to=reverse('posts_list'))
#     else:
#         form = NewPostForm()
#
#     return render(request, 'blog/post_create.html', context={'form': form})


class PostCreateView(generic.CreateView):
    model = Post
    form_class = NewPostForm
    template_name = "blog/post_create.html"


# def post_update_view(request,  pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect(to=reverse('posts_list'))
#     return render(request, 'blog/post_create.html', context={'form': form})


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = "blog/post_create.html"
    context_object_name = "form"


def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect(to=reverse('posts_list'))
    return render(request, 'blog/post_delete.html', context={'post': post})
