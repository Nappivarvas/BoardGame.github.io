from django import forms 

from .models import Game, Loan 

class GamesForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'owner', 'date_added']
        labels = {'name' : ''}


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['game', 'loaner', 'comment']
        labels = {'name' : ''}
        widgets = {'comment': forms.Textarea(attrs={'cols': 80})}