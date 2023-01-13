from django.urls import path

from players.views import add_player, list_players, add_match, list_matches, add_result, list_results

urlpatterns = [
    path('add-player/', add_player),
    path('list-players/', list_players),
    path('add-match/', add_match),
    path('list-matches/', list_matches),
    path('add-result/', add_result),
    path('list-results/', list_results),
]