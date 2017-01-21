from django.conf.urls import url, include
from django.contrib.auth.views import login

from . import views

app_name = 'discussions'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^view/(?P<user_id>\w+)/$', views.rep_view, name='rep_view'),
    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'discussions/login.html'
    }),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
        'template_name': 'discussions/logged_out.html'
    }),
    url(r'^sign_up/$', views.sign_up, name = 'sign_up'),
]
