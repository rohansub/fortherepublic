from django.conf.urls import url, include
from django.contrib.auth.views import login

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'discussions/login.html'
    }),
    url(r'^sign_up/$', views.sign_up, name = 'sign_up'),
]
