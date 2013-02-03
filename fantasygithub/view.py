from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404


def home(request):
    return render_to_response('views/index.html')

def manage(request):
    return render_to_response('views/manage.html')

def play(request):
    return render_to_response('views/play.html')

def about(request):
    return render_to_response('views/about.html')
