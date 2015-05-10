
import json
import requests
import os
r=requests.get('https://api.github.com/repos/twbs/bootstrap/releases')
a = json.loads(r.content)
link =  a[0]['assets'][0]['browser_download_url']

os.system('wget '+link)
