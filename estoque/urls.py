from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.produtos_list, name='produtos_list'),
    url(r'^produto/new/$', views.produto_new, name='produto_new'),
]