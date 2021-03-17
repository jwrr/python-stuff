#!/usr/bin/env python3
'''
Output git clone command for each project of user.
'''
import requests
import json
import sys

try:
  user = sys.argv[1]
except IndexError:
  sys.exit(f"usage: {sys.argv[0]} github_user_name")
  
url = f"https://api.github.com/users/{user}/repos"
projects = json.loads(requests.get(url).text)
for prj in projects:
  prj_url = prj["html_url"].replace("github", f"{user}@github")
  print(f"git clone {prj_url}")
  

