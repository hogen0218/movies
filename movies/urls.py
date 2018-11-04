"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
#两个serve :注意区分
from django.contrib.staticfiles import views   # 用静态文件的views.server
from django.views.static import serve    # 用媒体文件的 serve
from .settings import MEDIA_ROOT
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movies/', include('movie_details.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^static/(?P<path>.*)$', views.serve),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]
