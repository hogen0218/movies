from django.conf.urls import url
from .views import Index, Single


urlpatterns = [
    url(r'^index/$', Index.as_view(), name='movie_index'),
    url(r'^single/(?P<pk>\d+)/$', Single.as_view(), name='movie_single')
]