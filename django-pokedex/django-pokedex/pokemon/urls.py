from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_pokemon_list, name="get_pokemon_list"),
    path("add", views.add_pokemon, name="add_pokemon"), 
]