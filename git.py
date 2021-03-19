from github import Github
import os
from dotenv import load_dotenv
load_dotenv()
from contextlib import suppress

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

# using an access token
g = Github(ACCESS_TOKEN)

repos_branches={}   # Dictionary for branches
repos_status={}     # status of each repo
repos_protected={}  # each branch of a repo, protected or not
repos_collaborators={}  # usernames of collaborators
repos_collaborators_permissions={}  #permission level of each collaborator

for repo in g.get_user().get_repos():   # Get the repos
    repos_branches[repo.full_name]=list(repo.get_branches())    # store repo name: list of its branches in dict
    repos_status[repo.full_name]=repo.private   # store repo name: its status in dict

for i in repos_branches.keys():
    x=[]    # Initialize empty list
    for j in repos_branches[i]:     # Iterate through every repo's branches
        get_b = g.get_repo(i).get_branch(j.name)    # Fetch properties of each branch
        x.append(get_b.protected)   # Append if protected on not, False if not protected
    repos_protected[i]=x    # store repo name: protected or not for each of its branch
    

for i in repos_branches.keys():
    get_collab=g.get_repo(i).get_collaborators()    # get all collaborators of the repo
    arr=[]
    with suppress(Exception):   # To suppress 404 Not Found exception with ottosero/training-l1 repo
        for j in get_collab:
            repos_collaborators[i]=j.login    # store repo name: username in dict
            arr.append(g.get_repo(i).get_collaborator_permission(j.login))
    repos_collaborators_permissions[i]=arr     # store repo name: permissions of each user in dict


print(repos_status)

print(repos_branches)

print(repos_protected)

print(repos_collaborators)

print(repos_collaborators_permissions)
