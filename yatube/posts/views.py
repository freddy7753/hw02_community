from django.shortcuts import render, get_object_or_404
from .models import Post, Group

NOMBER_OF_POST:int = 10


def index(request):
    posts = Post.objects.order_by('-pub_date',)[:NOMBER_OF_POST]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by('-pub_date',)[:NOMBER_OF_POST]
    context = {
        'group': group,
        'posts': posts,
        'title': f'Записи сообщестава: {group}',
    }
    return render(request, 'posts/group_list.html', context)
