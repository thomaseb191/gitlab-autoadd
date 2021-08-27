from logging import error
import requests, sys
from requests.models import Response


if (len(sys.argv) != 2):
    error("Invalid arguments\nProgram should be run as such `python3 main.py <emails.csv>`")
    exit()
try:
    accountsfile = open(sys.argv[1], 'r')
except Exception as e: 
    print(e)
    exit()


gitlaburl = input("Enter Gitlab URL [Default is `https://gitlab.com`]: ")
if gitlaburl == "":
    gitlaburl = "https://gitlab.com"
gitlabgroup = input("Enter Gitlab Group: ")
accesslevel = input("Enter desired Gitlab Group access level [Default is 20]: ")
if accesslevel == "":
    accesslevel = "20"
accesstoken = input("Enter Private Access Token: ")

session = requests.Session()
session.headers.update({'PRIVATE-TOKEN': accesstoken})

for acc in accountsfile:
    email = acc.strip()
    query = {'email': email, 'access_level':accesslevel}
    response = session.post(gitlaburl + '/api/v4/groups/' + gitlabgroup + '/invitations', data=query)
    if (response.status_code == 201) and (response.json()['status'] == "success"):
        print(f'{email}: \033[92m SUCCESS: Invite Sent \033[0m')
    else:
        print(f'{email}: \033[91m FAIL \033[0m')
        print(response.json()['message'])    