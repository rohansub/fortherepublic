
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

from .models import AppUser, Politician, Issue

from django.db.models import Q

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            per = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],
                    email=form.cleaned_data['email'], first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'])
            app_user = AppUser(user=per, city_name=form.cleaned_data['city'], state=form.cleaned_data['state'])
            app_user.save()
            return render_index(app_user, None, request)
    form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('discussions/register.html', variables)

@login_required(login_url='/discussions/login/')
def index(request):
    app_user = AppUser.objects.get(user=request.user)
    return render_index(app_user, None, request)

@login_required(login_url='/discussions/login/')
def rep_view(request, user_id):
    app_user = AppUser.objects.get(user=request.user)
    u = User.objects.get(username=user_id)
    au = AppUser.objects.get(user=u)
    p = Politician.objects.get(user=au)
    return render_index(app_user, p, request)


@login_required(login_url='/discussions/login/')
def render_index(app_user, rep, request):
    template = loader.get_template('discussions/index.html')
    polys = Politician.objects.filter(Q(rep_location=app_user.city_name) | Q(rep_location=app_user.state))
    context = {
        'user' : app_user,
        'reps' : polys,
    }
    if(rep != None):
        issues = Issue.objects.filter(politician=rep)
        context['poly'] = rep
        context['issues'] = issues
    return HttpResponse(template.render(context, request))
