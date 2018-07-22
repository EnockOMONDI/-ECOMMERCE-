from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



app_name = 'shop'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^mens/', views.mens, name='mens'),
    url(r'^womens/', views.womens, name='womens'),
    url(r'^decorbeauty/', views.decorbeauty, name='decorbeauty'),
    url(r'^homeaccesories/', views.homeaccesories, name='homeaccesories'),
    url(r'^shop/', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
