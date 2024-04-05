import os
from github import Github
from github import Auth

# using an access token
auth = Auth.Token(os.environ["GH_PAT"])

# Public Web Github
gh = Github(auth=auth)

found_private = False
for repo in gh.get_repos():
    if repo.private:
        found_private = True

print("found private?", found_private, flush=True)
