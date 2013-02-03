from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import authenticate

@login_required
def manage(request):
    return render_to_response('views/manage.html', {'teams': []})

@login_required
def play(request):
    return render_to_response('views/play.html')

