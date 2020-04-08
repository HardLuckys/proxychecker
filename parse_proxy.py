import requests
from bs4 import BeautifulSoup as bs
import django
import sys, os
import re

project_dir = os.path.dirname(os.path.abspath(__file__)) + "\\proxychecker"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

django.setup()

from proxyapp.models import Proxy

def get_parse(link):
    session = requests.Session()
    parse = session.get(link)
    if parse.status_code == 200:
        results = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', parse.text)
        for result in results:
            if Proxy.objects.filter(ipadress=result).exists():
                return None
            else:
                proxy = Proxy()
                proxy.ipadress = result
                proxy.save()
