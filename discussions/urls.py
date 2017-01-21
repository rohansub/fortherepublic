from django.conf.urls import url, include
from django.contrib.auth.views import login

from . import views

app_name = 'discussions'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^view/(?P<user_id>\w+)/$', views.rep_view, name='rep_view'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^sign_up/$', views.sign_up, name = 'sign_up'),
]
