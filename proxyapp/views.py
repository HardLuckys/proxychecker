from django.shortcuts import render
from .tasks import hello_people, check_proxy_task



def lol(request):
    hello_people.delay()
    check_proxy_task.delay()
    lol = 'Hi'
    context = {
        'lol': lol
    }
    return render(request, 'lol.html', context)
