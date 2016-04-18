import config
import requests
import urllib

head = {'Authorization': 'token %s' % TOKEN}
def r(str):
  requests.get(BASE+str, headers = head).json()

fileDownloadURL = pprint(r('repos/'+r('orgs/'+ORG+'/repos')[0]['full_name']+'/contents')[0]['download_url'])
contentsRepo = requests.get(BASE+'repos/'+requests.get(BASE+'orgs/'+ORG+'/repos', headers = head).json()[0]['full_name']+'/contents', headers = head).json()
for fileOrDir in contentsRepo:

i = 0
while i<len(contentsRepo):
  if(contentsRepo[i]['type'] == 'dir'):
    print("Extending " + contentsRepo[i]['_links']['self'] + ' ' + str(i) + ' of ' + str(len(contentsRepo)))
    contentsRepo += requests.get(contentsRepo[i]['_links']['self'], headers = head).json()
  i = i+1

filesN = filter(lambda k: k['type']=='file', contentsRepo)

def isPython(name):
  return name[-3:]=='.py'

for i in range(len(contentsRepo)):
  if(contentsRepo[i]['type']=='file' and isPython(contentsRepo[i]['name'])):
    print(contentsRepo[i]['name'], contentsRepo[i]['download_url'])

target_url = 'https://raw.githubusercontent.com/ITUPythonStudyGroup/KickScrapePractice/master/adrianbrink/scraper.py'
txt = urllib.request.urlopen(target_url).read()
