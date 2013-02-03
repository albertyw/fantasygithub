"""
This file interacts with github
"""
import os
import sys 
parent_path = os.path.dirname(os.path.realpath(__file__))+'/../../'
sys.path.append(parent_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "util.settings")

import datetime
from pygithub3 import Github

from fantasygithub.models.models import Dev, Commit

user = 'albertyw'
token = 'f8b5faa6fcc0f772480e23418af5b04b1879640b'

class GitInfo():
    def __init__(self, token):
        self.gh = Github(token=token)
    
    """
    Get a list of repos of a user
    """
    def get_user_repos(self, user):
        # Get repositories of a user
        repos = self.gh.repos.list(user=user)
        all_repos = []
        for page in repos:
            all_repos += list(page)
        return all_repos
        
    """
    Get a list of commits by the user
    """
    def get_user_commits(self, user):
        repos = self.get_user_repos(user)
        all_commits = []
        for repo in repos:
            try:
                commits = self.gh.repos.commits.list(user=repo.owner.login, repo=repo.name)
            except:
                continue
            all_commits += commits.all()
        return all_commits
        
    """
    Save commits
    """
    def save_commits(self, user, commits, search_time):
        dev = self.get_dev(user)
        for commit in commits:
            if len(Commit.objects.filter(sha=commit.sha)) != 0:
                continue
            commit_object = Commit()
            commit_object.dev = dev
            commit_object.time = commit.commit.author.date
            commit_object.sha = commit.sha
            commit_object.save()
        dev.last_updated = search_time
        dev.save()
        
    """
    Find or make a dev
    """
    def get_dev(self, user):
        try:
            return Dev.objects.get(login=user)
        except:
            user = self.gh.users.get(user)
            dev = Dev(login=user, avatar_url=user.avatar_url)
            dev.save()
            return dev
        
    """
    Get all commits between dates
    """
    def get_user_commits_dates(self, user, start_date, end_date):
        return None
    
    def test(self):
        return None
        
a = GitInfo(token)
print a.test()
commits = a.get_user_commits('hrs')
a.save_commits('hrs', commits, datetime.datetime.now())


