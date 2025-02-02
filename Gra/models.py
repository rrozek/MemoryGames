from django.db import models
from random import shuffle

cards = [(4, "4 cards"), (8, "8 cards"), (16, "16 cards"), (32, "32 cards")]


def create_playboard(cards_no, row_len=8):
    deck = 2 * list(range(int(0.5 * cards_no)))  # tworzymy talie kart
    shuffle(deck)  # tasowanie
    split_list = []
    temp_list = []

    for i, val in enumerate(deck):
        temp_list.append({"card": val, "found": False})
        if (i + 1) % row_len == 0:
            split_list.append(temp_list)
            temp_list = []

    # Add the remaining elements if the length is not divisible by row_length
    if temp_list:
        split_list.append(temp_list)
    return split_list


class NewGame(models.Model):
    player1 = models.CharField(max_length=15, blank=True)
    player2 = models.CharField(max_length=15, blank=True)
    number_cards = models.IntegerField(choices=cards)
    playboard = models.JSONField(blank=True, null=True)  # generuje sie jako pusty
    # curent_playboard =
    moves = models.IntegerField(default=0)  # pole liczące ruchy graczy
    winner = models.CharField(max_length=15, blank=True, null=True)
    scoreplayer1 = models.IntegerField(blank=True, null=True, default=0)
    scoreplayer2 = models.IntegerField(blank=True, null=True, default=0)

    def save(self, *args, **kwargs):
        if not self.playboard:
            self.playboard = create_playboard(self.number_cards)
        super().save(*args, **kwargs)

    # number_cards = models.DecimalField(default=10 , max_digits=20, decimal_places=0)

    # Nadpisywanie funkcji save do sprawdzeniam - do sprawdzenia. podczas zapisywania modelu tworzy się plansza!! W klasie name NADPISYWANIE FUNKCJI SAVE W DJANGO!!
    # POLE PLANSZA
    # BLANCK
    # w trakcie swywołania funkcji save w tworzy sie playground


# Create your models here.
