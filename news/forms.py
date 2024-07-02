from .models import News_post
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'username', 'short_description', 'text', 'pub_date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Введите заголовок'}),
            'username': TextInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Введите имя автора'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'id': 'description', 'placeholder': 'Введите краткое описание новости'}),
            'text': Textarea(attrs={'class': 'form-control', 'id': 'content', 'rows': '5', 'placeholder': 'Введите содержание'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'id': 'date', 'placeholder': 'Введите дату публикации'})
        }






