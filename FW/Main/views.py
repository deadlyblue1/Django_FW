from django.shortcuts import render, redirect
from .models import pages
from .forms import pagesform


def index(request):
    return render(request,"Main/index.html")


def about(request):
    return render(request,"Main/about.html")


def page(request):
    page_list = pages.objects.all()
    return render(request,"Main/pages.html",{'title':'Главная страница сайта','page':page_list})


def create_page(request):
    error = ''
    if request.method == 'POST':
        form = pagesform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages')
        else:
            error = 'Форма заполнена неправильно!'
    form = pagesform()
    context = {
        'form': form,
        'error': error
    }
    return render(request,"Main/create_page.html",context)


