from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Game


def index(request):
    """The home page for BoardGames"""
    return render(request, 'Boardgame.github.io/index.html')

@login_required
def games(request):
    """Shows all games"""
    games = Game.objects.filter(owner=request.user).order_by('name')
    context = {'games' : games}
    return render(request, 'BoardGames.github.io/games.html', context)