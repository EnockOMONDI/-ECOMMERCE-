from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create')
]
