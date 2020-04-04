from django.conf.urls import include,url
from django.urls import path
from apps.login.views import *
app_name = 'login'

urlpatterns = [
    path('mainpage', mainpage, name='mainpage'),

]
