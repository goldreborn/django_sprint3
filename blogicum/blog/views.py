from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from .models import Post
from django.db.models import Q
from django.utils import timezone

now = timezone.now()


def index(request):
    template = 'blog/index.html'

    post_data = Post.objects.all().filter(
        Q(is_published=True) &
        Q(pub_date__lte=now) &
        Q(category__is_published=True)
    ).order_by('id')[:5]

    context = {'post_list': post_data}

    return render(request, template, context)


def post_detail(request, post_id):

    template = 'blog/detail.html'

    post = get_object_or_404(
        Post.objects.filter(
            is_published__exact=True,
            pub_date__lte=now,
            category__is_published__exact=True
        ),
        pk=post_id
    )

    context = {'post': post}

    return render(request, template, context)


def category_posts(request, category_slug):

    template = 'blog/category.html'

    category_info = {
        'title': Post.objects.values(
            'category__title'
        ).filter(
            category__slug=category_slug
        ).first()['category__title'],

        'description': Post.objects.values(
            'category__description'
        ).filter(
            category__slug=category_slug
        ).first()['category__description']
    }

    posts_in_category = Post.objects.filter(
        Q(category__slug=category_slug) &
        Q(pub_date__lte=now) &
        Q(is_published=True)
    )

    query_set = get_list_or_404(
        posts_in_category,
        category__is_published=True
    )

    context = {
        'category': category_info,
        'post_list': query_set
    }

    return render(request, template, context)
