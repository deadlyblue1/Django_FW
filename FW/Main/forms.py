from .models import pages
from django.forms import ModelForm,TextInput,Textarea


class pagesform(ModelForm):
    class Meta:
        model = pages
        fields = ["title", "text"]
        widgets = {'title': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название'
        }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст'
            })}
