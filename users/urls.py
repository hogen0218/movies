from django.conf.urls import url
from users.views import Register

urlpatterns = [
    url(r'^register/', Register.as_view(), name='register'),
]
