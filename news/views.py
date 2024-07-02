from django.shortcuts import render, redirect
from . models import News_post
from .forms import News_postForm

def home(request):
    all_news = News_post.objects.all()
    news = all_news[::-1]
    context = {
        'caption': 'CatDjango',
        'page': 'Новости',
        'nav_data': {
            'home': 'Главная страница',
            'data': 'Руководство по Django',
            'test': 'Блог о кошках',
            'fourth': 'Форум сообщества',
            'news': 'Новости',
            'add_news': 'Добавить новость'
        },
        'news': news
    }
    return render(request, 'news/news.html', context)

def create_news(request):
    error = ""
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Данные заполнены некорректно'
    form = News_postForm()
    context = {
        'caption': 'CatDjango',
        'page': 'Новости',
        'nav_data': {
            'home': 'Главная страница',
            'data': 'Руководство по Django',
            'test': 'Блог о кошках',
            'fourth': 'Форум сообщества',
            'news': 'Новости',
            'add_news': 'Добавить новость'
        },
        'form': form,
        'error': error
    }
    return render(request, 'news/add_new_post.html', context)