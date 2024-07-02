from django.shortcuts import render

def index(request):
    context = {
        'caption': 'CatDjango',
        'page': 'Главная страница',
        'nav_data': {
            'home': 'Главная страница',
            'data': 'Руководство по Django',
            'test': 'Блог о кошках',
            'fourth': 'Форум сообщества',
            'news': 'Новости',
            'add_news': 'Добавить новость'
        }
    }
    return render(request, 'main/index.html', context)

def data(request):
    context = {
        'caption': 'CatDjango',
        'page': 'Руководство по Django',
        'nav_data': {
            'home': 'Главная страница',
            'data': 'Руководство по Django',
            'test': 'Блог о кошках',
            'fourth': 'Форум сообщества',
            'news': 'Новости',
            'add_news': 'Добавить новость'
        }
    }
    return render(request, 'main/data.html', context)

def test(request):
    context = {
        'caption': 'CatDjango',
        'page': 'Блог о кошках',
        'nav_data': {
            'home': 'Главная страница',
            'data': 'Руководство по Django',
            'test': 'Блог о кошках',
            'fourth': 'Форум сообщества',
            'news': 'Новости',
            'add_news': 'Добавить новость'
        }
    }
    return render(request, 'main/test.html', context)

def four(request):
    context = {
        'caption': 'CatDjango',
        'page': 'Форум сообщества',
        'nav_data': {
            'home': 'Главная страница',
            'data': 'Руководство по Django',
            'test': 'Блог о кошках',
            'fourth': 'Форум сообщества',
            'news': 'Новости',
            'add_news': 'Добавить новость'
        }
    }
    return render(request, 'main/fourth.html', context)

def footer(request):
    context = {
        'caption': 'CatDjango',
        'nav_data': {
            'home': 'Главная страница',
            'data': 'Руководство по Django',
            'test': 'Блог о кошках',
            'fourth': 'Форум сообщества',
            'news': 'Новости',
            'add_news': 'Добавить новость'
        }
    }
    return render(request, 'main/footer.html', context)

# def nav(request):
#     context = {
#         'caption': 'CatDjango',
#         'nav_data': {
#             'home': 'Главная страница',
#             'data': 'Руководство по Django',
#             'test': 'Блог о кошках',
#             'fourth': 'Форум сообщества',
#             'news': 'Новости',
#             'add_news': 'Добавить новость'
#         }
#     }
#     return render(request, 'main/nav.html', context)


