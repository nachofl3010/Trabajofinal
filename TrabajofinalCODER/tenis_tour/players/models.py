from django.db import models

class Players(models.Model):
    name= models.CharField(max_length=100)
    age= models.IntegerField()
    country=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Matches(models.Model):
    CHOICES=(
        ('Player 1', 'Player 1'),
        ('Player 2', 'Player 2'),
    )
    player_1=models.CharField(max_length=100)
    player_2=models.CharField(max_length=100)
    year=models.IntegerField()
    winner=models.CharField(choices=CHOICES, max_length=8)

class Results(models.Model):
    name=models.CharField(max_length=100)
    tournament=models.CharField(max_length=100)
    result=models.CharField(max_length=100)
    points_earned=models.IntegerField()

