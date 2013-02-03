from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from fantasygithub.models import Team
from fantasygithub.github import GitInfo
from django.template import RequestContext
import json

@login_required
def manage(request):
    if request.method == 'POST':
        if 'create_team' in request.POST:
            team = Team()
            team.manager = request.user
            team.name = request.POST['name']
            team.save()
            
            git = GetInfo()
            dev_usernames = json.loads(request.POST['devs'])
            for dev_username in dev_usernames:
                if git.is_dev(dev_username):
                    dev = git.get_dev(dev_username)
                    dev.teams.add(team)
                    dev.save()
            return HttpResponse('done')
        if 'check_dev' in request.POST:
            a = GitInfo()
            return HttpResponse(str(a.is_dev(request.POST['username'])))
        if 'delete_team' in request.POST:
            team_name = request.POST['name']
            team = Team.objects.filter(name=team_name, manager=request.user)
            if len(team) != 0:
                team.delete()
        
        
    teams = []
    for team in Team.objects.filter(manager=request.user).all():
        teams += team.name
    print teams
    return render_to_response('views/manage.html', {'teams': teams}, context_instance=RequestContext(request),)

@login_required
def play(request):
    if request.method == 'POST':
        #if 'POST' in request.POST
        pass
    teams = []
    for team in Team.objects.filter(manager=request.user).all():
        teams += team.name
    print teams
    return render_to_response('views/play.html', {'teams': teams}, context_instance=RequestContext(request))
