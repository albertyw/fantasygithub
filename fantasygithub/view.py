from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from fantasygithub.models import Team
from django.template import RequestContext

@login_required
def manage(request):
    if request.method == 'POST':
        #if 'POST' in request.POST
        pass
    teams = []
    for team in Team.objects.filter(manager=request.user).all():
        teams += team.name
    print teams
    return render_to_response('views/manage.html', {'teams': teams}, context_instance=RequestContext(request),)

@login_required
def play(request):
    return render_to_response('views/play.html', context_instance=RequestContext(request))

