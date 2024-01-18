from django.shortcuts import render, get_object_or_404

from django.utils import timezone
from .models import Post, Category

POSTS_ON_MAIN = 5


def get_query_set():

    q_set = Post.objects.select_related().filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )

    return q_set


def index(request):

    template = 'blog/index.html'

    post_data = get_query_set()[:POSTS_ON_MAIN]

    context = {'post_list': post_data}

    return render(request, template, context)


def post_detail(request, post_id):

    template = 'blog/detail.html'

    post = get_object_or_404(
        get_query_set(),
        pk=post_id
    )

    context = {'post': post}

    return render(request, template, context)


def category_posts(request, category_slug):

    template = 'blog/category.html'

    objects = get_object_or_404(
        Category.objects.values(
            'title',
            'description'
        ).filter(
            is_published=True
        ), slug=category_slug
    )

    category_info = objects

    query_set = get_query_set().filter(
        category__slug=category_slug
    )

    context = {
        'category': category_info,
        'post_list': query_set
    }

    return render(request, template, context)
