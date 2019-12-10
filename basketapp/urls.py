from django.urls import path
from basketapp.views import *

app_name = 'basketapp'

urlpatterns = [
    path('', basket_view, name='view'),
    path('add/<int:pk>/', basket_add_view, name='add'),
    path('remove/<int:pk>/', basket_remove_view, name='remove'),
]