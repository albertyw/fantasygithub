from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from fantasygithub.models import Team
from fantasygithub.github import GitInfo
from django.template import RequestContext

@login_required
def manage(request):
    if request.method == 'POST':
        if 'create_team' in request.POST:
            a = Team()
            a.manager = request.user
            a.name = request.POST['name']
            a.save()
            return HttpResponse('done')
        if 'check_dev' in request.POST:
            a = GitInfo()
            return HttpResponse(str(a.is_dev(request.POST['username'])))
        
        
    teams = []
    for team in Team.objects.filter(manager=request.user).all():
        teams += team.name
    print teams
    return render_to_response('views/manage.html', {'teams': teams}, context_instance=RequestContext(request),)

@login_required
def play(request):
    return render_to_response('views/play.html', context_instance=RequestContext(request))

