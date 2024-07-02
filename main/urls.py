from django.urls import path
from . import views
# точка . означает import из этой же директории, где файл main/urls.py

urlpatterns = [
    path('', views.index, name='home'),
    path('data', views.data, name='data'),
    path('test', views.test, name='test'),
    path('four', views.four, name='fourth')
    ]
