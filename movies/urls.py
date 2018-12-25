from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^movies/$', views.movie_list, name='movie_list'),
    path('details/<id>', views.details, name='details')
]
