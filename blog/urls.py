
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.post_list, name='post_list'),  
    
    path('post_list.html', views.post_list, name='post_list'),

    path('about.html', views.about, name='about'),

    path('contact.html', views.contact, name='contact'),

    path('shop-single.html', views.shop_single, name='shop_single'),

    path('shop.html', views.shop, name='shop'),
]
