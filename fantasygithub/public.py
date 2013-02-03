from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, UserCreationForm
from django.template import RequestContext

def home(request):
    return render_to_response('views/index.html')

def login_page(request):
    errors = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('fantasygithub.view.manage'))
            else:
                errors = 'Disabled login'
        else:
            errors = 'Invalid login'
    form = AuthenticationForm(request)
    return render_to_response('views/login.html',
        {'form': form,
         'errors': errors}, context_instance=RequestContext(request),
        )

def logout_page(request):
    logout(request)
    return render_to_response('views/index.html')

def about(request):
    return render_to_response('views/about.html')
