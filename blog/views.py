from django.shortcuts import render
from django.http import HttpResponse


def post_list_view(request):
    return HttpResponse('posts_list')

