from django.conf.urls import include,url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from login import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('apps.login.urls',namespace='login')),
    url(r'^', views.Index.as_view(), name='index'),
    #url(r'^myadmin', include('apps.myadmin.urls',namespace='myadmin')),
    #url(r'^', views.Index.as_view(), name='index'),
]
urlpatterns += staticfiles_urlpatterns()
