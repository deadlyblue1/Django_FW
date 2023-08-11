from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='menu'),
    path('about',views.about,name='about'),
    path('pages', views.page,name='pages'),
    path('create_page', views.create_page,name='create_page')
]