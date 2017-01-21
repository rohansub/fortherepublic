
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .forms import RegistrationForm

#from logic import *

from django.template import RequestContext

from .models import AppUser

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            per = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],
                    email=form.cleaned_data['email'], first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'])
            app_user = AppUser(user=per, city_name=form.cleaned_data['city'], state=form.cleaned_data['state'])
            app_user.save()
            return render_to_response('discussions/index.html')
    form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('discussions/register.html',variables)

def index(request):
    return HttpResponse("You at the index")
