from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    # The name of the game and who owns it.
    name = models.Charfield(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # Keeps track of when the game is added
    date_added = models.DateTimeField(auto_now_add=True)
    # Keeps track of the date of the loan
    date_loaned = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    



