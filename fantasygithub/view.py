from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from fantasygithub.models import Team

@login_required
def manage(request):
    if request.method == 'POST':
        pass
    teams = []
    for team in Team.objects.filter(manager=request.user).all():
        teams += team.name
    return render_to_response('views/manage.html', {'teams': []})

@login_required
def play(request):
    return render_to_response('views/play.html')

