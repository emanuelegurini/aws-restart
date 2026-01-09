# D&D Character Generator CLI - Appunti

## Cosa vogliamo fare

- Un'app da terminale per generare personaggi D&D, in Python
- L'utente descrive il tipo di personaggio che vuole
- Gemini genera tutto: nome, razza, classe, stats, backstory, descrizione fisica
- I personaggi li salviamo in `db.json` nella stessa cartella dello script

## API da usare

- **Gemini** — per generare tutti i dettagli del personaggio basandosi sulla descrizione dell'utente

## Concetti principali

- **Personaggio** — un PG completo con nome, razza, classe, stats, backstory
- **Descrizione** — input testuale dell'utente (es: "un mago misterioso con un passato oscuro")
- **Stats** — i 6 attributi: FOR, DES, COS, INT, SAG, CAR (valori da 3 a 18)

## Cosa deve fare

### Generazione
- generare personaggio da una descrizione testuale dell'utente
- Gemini deve restituire: nome, razza, classe, stats, backstory, descrizione fisica
- rigenerare un personaggio con una nuova descrizione

### Gestione personaggi
- salvare personaggio generato
- vedere lista personaggi salvati
- vedere dettaglio di un personaggio
- cancellare personaggio
- rigenerare solo la backstory di un personaggio esistente

## Struttura dati

```json
{
  "characters": [
    {
      "id": "uuid",
      "user_prompt": "un mago misterioso con un passato oscuro",
      "name": "Eldrin Moonwhisper",
      "race": "Elfo",
      "class": "Mago",
      "level": 1,
      "stats": {
        "strength": 8,
        "dexterity": 14,
        "constitution": 12,
        "intelligence": 17,
        "wisdom": 13,
        "charisma": 10
      },
      "backstory": "Nato nella biblioteca di Silverymoon...",
      "physical_description": "Alto e slanciato, capelli argentati...",
      "created_at": "2025-01-09T10:30:00"
    }
  ]
}
```

## Note

- Se `db.json` non esiste, crearlo vuoto al primo avvio
- Il prompt a Gemini deve chiedere di restituire dati strutturati (JSON) per poterli salvare
- Stats devono essere coerenti con razza e classe (es: un mago avrà INT alta)
- Salvare anche il prompt originale dell'utente per riferimento
- Output leggibile con emoji (⚔️ guerriero, 🧙 mago, 🧝 elfo, etc.)
- Mostrare stats con barre visuali (███░░ 14)
- Messaggi chiari per errori (personaggio non trovato, API non raggiungibile, etc.)
