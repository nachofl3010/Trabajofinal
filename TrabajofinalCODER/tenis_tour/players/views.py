
from django.shortcuts import render

from django.http import HttpResponse
from players.models import Players, Matches, Results
from players.forms import PlayerForm, ResultForm

def add_player(request):
    if request.method == 'GET':
        context = {
            'form': PlayerForm()
        }

        return render(request, 'players/add_player.html', context=context)

    elif request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            Players.objects.create(
                name=form.cleaned_data['name'],
                country=form.cleaned_data['country'],
                is_active=form.cleaned_data['is_active'],
                age=form.cleaned_data['age']
            )
            context = {
                'message': 'Player added successfully'
            }
            return render(request, 'players/add_player.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': PlayerForm()
            }
            return render(request, 'players/add_player.html', context=context)

def list_players(request):
    if 'search' in request.GET:
        search = request.GET['search']
        players = Players.objects.filter(name__icontains=search)
    else:
        players = Players.objects.all()
    context = {
        'players':players,
    }
    return render(request, 'players/list_players.html', context=context)


def add_match(request):
    new_match=Matches.objects.create(player_1='Roger Federer',player_2='Rafael Nadal',year=2017,winner= 'Player 1')
    return HttpResponse('Match has been added')

def list_matches(request):
    all_matches=Matches.objects.all()
    context={
        'matches':all_matches
    }
    return render(request, 'matches/list_matches.html', context=context)



def add_result(request):
    if request.method == 'GET':
        context = {
            'form': ResultForm()
        }

        return render(request, 'results/add_result.html', context=context)

    elif request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            Results.objects.create(
                name=form.cleaned_data['name'],
                tournament=form.cleaned_data['tournament'],
                result=form.cleaned_data['result'],
                points_earned=form.cleaned_data['points_earned']
            )
            context = {
                'message': 'Result added successfully'
            }
            return render(request, 'results/add_result.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': ResultForm()
            }
            return render(request, 'results/add_result.html', context=context)

def list_results(request):
    all_results=Results.objects.all()
    context={
        'results':all_results
    }
    return render(request, 'results/list_results.html', context=context)