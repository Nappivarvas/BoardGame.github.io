from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Game, Loan
from .forms import GamesForm, LoanForm


def index(request):
    """The home page for BoardGames"""
    return render(request, 'board_game/index.html')

@login_required
def games(request):
    """Shows all games"""
    games = Game.objects.filter(owner=request.user).order_by('name')
    context = {'games' : games}
    return render(request, 'board_game/games.html', context)


@login_required
def add_game(request):
    """Add a new game."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = Game()
    else:
        # POST data submitted; process data.
        form = GamesForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_game:games')
        # Display a blank or invalid form.
        context = {'form' : form}
        return render(request, 'board_game/add_game.html', context)
    

@login_required
def loan(request):
    """Mark a game as loaned by user."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = LoanForm()
    else:
        # POST data submitted; process data.
        form = LoanForm(data=request.POST)
        if form.is_valid():
            submit = form.save(commit=False)
            submit.games = games
            submit.save()
            return redirect('board_game:games')
    
    # Display a blank or invalid form
    context = {'games': games, 'form': form}
    return render(request, 'board_game/loan.html', context)

