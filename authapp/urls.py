from django.urls import path
from authapp.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'authapp'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('edit/', edit_view, name='edit'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)