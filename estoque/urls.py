from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    #url(r'^$', views.produtos_list, name='produtos_list'),

    url(r'^$', views.index, name='pagina_inicial'),
    url(r'^produto/list', views.produtos_list, name='produtos_list'),
    url(r'^produto/new/$', views.produto_new, name='produto_new'),
    url(r'^compra/list', views.compras_list, name='compras_list'),
    #url(r'^compra/new/$', views.compras_new, name='compras_new'),
    #url(r'^compra/new/$', views.itens_view, name='itens_view'),
    url(r'^compra/new/$', views.compra, name='compra'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]