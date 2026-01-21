from django.db import IntegrityError, OperationalError
from django.shortcuts import render
from .models import Pokemon
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt 
@require_POST
def add_pokemon(request):
    try:
        data = json.loads(request.body)
        
        pokemon = Pokemon.objects.create(
            name=data['name'], 
            pokedex_id=data['pokedex_id']
        )
        
        return JsonResponse({
            'id': pokemon.id, 
            'name': pokemon.name, 
            'pokedex_id': pokemon.pokedex_id
        }, status=201)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON non valido'}, status=400)
    
    except KeyError as e:
        return JsonResponse({'error': f'Campo mancante: {e}'}, status=400)
    
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Tipo di dato non valido'}, status=400)
    
    except IntegrityError:
        return JsonResponse({'error': 'Pokemon già esistente'}, status=409)
    
    except OperationalError:
        return JsonResponse({'error': 'Database non disponibile'}, status=503)
    
    except Exception as e:
        return JsonResponse({'error': 'Errore interno del server'}, status=500)

@require_GET
def get_pokemon_list(request):
    try:
        pokemon_list = list(Pokemon.objects.all().values())
        return JsonResponse(pokemon_list, safe=False)
    
    except OperationalError:
        # Problemi di connessione al database
        return JsonResponse({'error': 'Database non disponibile'}, status=503)
    
    except Exception as e:
        # Errore generico imprevisto
        return JsonResponse({'error': str(e)}, status=500)