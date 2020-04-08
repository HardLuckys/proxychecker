import requests
import urllib3
import django
import sys, os
from django.core.exceptions import ObjectDoesNotExist

project_dir = os.path.dirname(os.path.abspath(__file__)) + "\\proxychecker"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

django.setup()

from proxyapp.models import Proxy

URL = "http://google.com"
TIMEOUT = (3.05,27)

def check_proxy(proxy):
    try:
        Proxy.objects.get(ipadress=proxy)
    except Proxy.DoesNotExist as e:
        return print(e)
    try:
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        session.max_redirects = 300
        #proxy = proxy.split('\n',1)[0]
        #print('Checking ' + proxy)
        session.get(URL, proxies={'http':'http://' + proxy}, timeout=TIMEOUT,allow_redirects=True)
        return True

    except requests.exceptions.ConnectionError as e:
        Proxy.objects.get(ipadress=proxy).delete()
        print('Error! deleted: ', proxy)
        return e
    except requests.exceptions.ConnectTimeout as e:
        Proxy.objects.get(ipadress=proxy).delete()
        print('Error,Timeout! deleted: ', proxy)
        return e
    except requests.exceptions.HTTPError as e:
        Proxy.objects.get(ipadress=proxy).delete()
        print('HTTP ERROR! deleted: ', proxy)
        return e
    except requests.exceptions.Timeout as e:
        Proxy.objects.get(ipadress=proxy).delete()
        print('Error! Connection Timeout! deleted: ', proxy)
        return e
    except urllib3.exceptions.ProxySchemeUnknown as e:
        Proxy.objects.get(ipadress=proxy).delete()
        print('ERROR unkown Proxy Scheme! deleted: ', proxy)
        return e
    except requests.exceptions.TooManyRedirects as e:
        Proxy.objects.get(ipadress=proxy).delete()
        print('ERROR! Too many redirects! deleted: ', proxy)
        return e
