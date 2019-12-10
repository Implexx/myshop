from django.contrib import admin
from django.urls import path
from mainapp.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainapp'

urlpatterns = [
    path('', main_view, name='main'),
    path('about/', about_view, name='about'),
    path('account/', account_view, name='account'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('contact/', contact_view, name='contact'),
    path('my_account/', my_account_view, name='my_account'),
    path('product_details/', product_details_view, name='product_details'),
    # path('products/', products_view, name='products'),
    path('category/', products_view, name='category'),
    path('category/<int:pk>/', products_view, name='category'),
    path('shop/', shop_view, name='shop'),
    path('shop_list/', shop_list_view, name='shop_list'),
    path('wishlist', wishlist_view, name='wishlist'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)