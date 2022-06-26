from django.shortcuts import render, get_object_or_404

from .models import Post, Group

TEN = 10

def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию
    # (от больших значений к меньшим)
    posts = Post.objects.all()[:TEN]
    # В словаре context отправляем информацию в шаблон
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:TEN]
    title = f'Записи сообщества {group}'
    context = {
        'group': group,
        'posts': posts,
        'slug': slug,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)
