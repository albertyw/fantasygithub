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

class GitInfo():
    def __init__(self):
        token = 'f8b5faa6fcc0f772480e23418af5b04b1879640b'
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
            # TODO this should call __save_commits in order to not hit github too much
            try:
                commits = self.gh.repos.commits.list(user=repo.owner.login, repo=repo.name)
            except:
                continue
            all_commits += commits.all()
        return all_commits
        
    """
    Save commits
    """
    def __save_commits(self, user, commits, search_time):
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
            return Dev.objects.get(username=user)
        except:
            user = self.gh.users.get(user)
            dev = Dev(username=user, avatar_url=user.avatar_url)
            dev.save()
            return dev
            
    """
    Check whether a string is a valid dev username
    """
    def is_dev(self, username):
        try:
            self.gh.users.get(username)
            return True
        except:
            return False
        
    """
    Get all commits between dates
    """
    def get_user_commits_dates(self, user, start_date, end_date):
        # TODO 
        return None
    
a = GitInfo()
print a.is_dev('albertyw')
commits = a.get_user_commits('albertyw')
print len(commits)
#a.save_commits('hrs', commits, datetime.datetime.now())


