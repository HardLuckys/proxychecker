from proxychecker.celery import app
from .hello import hello
from parse_proxy import get_parse
from ckeck import check_proxy
from .models import Proxy


@app.task
def hello_people():
    for proxy in proxy_list():
        get_parse(proxy)


@app.task
def check_proxy_task():
    proxis = Proxy.objects.all()
    for proxy in proxis:
        check_proxy(str(proxy))
