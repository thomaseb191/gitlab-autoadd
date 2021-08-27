import requests, sys
from requests.models import Response

session = requests.Session()
session.headers.update({'PRIVATE-TOKEN': sys.argv[1]})
#print(len(response.json()))

studentsfile = open('students.csv', 'r')

success = 0
fail = 0

for student in studentsfile:
    query = {'email': student.strip(), 'access_level':'20'}
    response = session.post('https://coursework.cs.duke.edu/api/v4/groups/ece-cs-250-fall-2021/invitations', data=query)
    if (response.status_code == 200):
        print(f'{student.strip()}: \033[92m SUCCESS \033[0m')
    else:
        print(f'{student.strip()}: \033[91m FAIL \033[0m')
        print(response.reason)    