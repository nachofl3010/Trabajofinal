from django.shortcuts import render

from django.http import HttpResponse
from tournaments.models import Tournaments

def add_tournament(request):
    new_tournament = Tournaments.objects.create(category='M1000',name='Miami ATP Masters')
    return HttpResponse('Tournament has been added')

def list_tournaments(request):
    all_tournaments=Tournaments.objects.all()
    context={
        'tournaments':all_tournaments
    }
    return render(request, 'tournaments/list_tournaments.html', context=context)


