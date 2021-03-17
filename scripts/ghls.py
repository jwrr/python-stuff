#!/usr/bin/env python3
'''
Output all project of user.
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
  prj_url = prj["html_url"]
  print(f"{prj_url}")
  

