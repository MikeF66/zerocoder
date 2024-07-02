from django.urls import path
from . import views
# точка . означает import из этой же директории, где файл main/urls.py

urlpatterns = [
    path('', views.home, name='news_home'),
    path('create_news/', views.create_news, name='add_news')
    ]