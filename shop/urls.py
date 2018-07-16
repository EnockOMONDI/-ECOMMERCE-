from django.conf.urls import url
from . import views


app_name = 'shop'

urlpatterns = [
    url(r'^shop/$', views.home, name='home'),
    url(r'^shop/$', views.about, name='about'),
    url(r'^shop/$', views.mens, name='mens'),
    url(r'^shop/$', views.womens, name='womens'),
    url(r'^shop/$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
