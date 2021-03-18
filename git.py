from github import Github
import os
from dotenv import load_dotenv
load_dotenv()

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

# using an access token
g = Github(ACCESS_TOKEN)

repos_branches={}
p=[]

for repo in g.get_user().get_repos():
    repos_branches[repo.name]=list(repo.get_branches())
    # print(repo.private)

print(repos_branches)

get_b=g.get_repo('ottosero/dynamo-training').get_branch('AY-develop')
print(get_b.protected)

t=g.get_repo('ottosero/dynamo-training').get_collaborators()
for i in t:
    print(i.login)
print(g.get_repo('ottosero/dynamo-training').get_collaborator_permission('ottosero-keysersoze'))