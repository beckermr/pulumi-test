import os
from github import Github
from github import Auth

# using an access token
auth = Auth.Token(os.environ["GH_PAT"])

# Public Web Github
gh = Github(auth=auth)

repo = gh.get_repo("beckermr/cv")

print(repo)
