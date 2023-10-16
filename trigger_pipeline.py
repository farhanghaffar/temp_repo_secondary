import os

from github import Github
from github import Auth


owner = 'FarhanGhaffar'
repo_name = 'temp_repo_secondary'
workflow_id = '72571241'
main_branch = 'main'


print("it worked")
# g = Github(os.environ.get('github-token'))
# # print(os.environ.get('GITHUB_TOKEN'))
# repo = g.get_user(owner).get_repo(repo_name)

# workflow_runs = repo.get_workflow_runs(event = 'queued')

# # if workflow_runs.totalCount == 0:
# repo.get_workflow(workflow_id).create_dispatch(ref=main_branch)
