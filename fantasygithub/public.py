from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, UserCreationForm

def home(request):
    return render_to_response('views/index.html')

def login(request):
    form = AuthenticationForm(request)
    return render_to_response('views/login.html', 
        {'form': form},
        )

def about(request):
    return render_to_response('views/about.html')
