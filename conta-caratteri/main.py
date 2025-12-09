"""
CONTACARATTERI

DOMINIO:
=========

1. INPUT - Sorgente del testo
   - Lettura da file di testo (.txt)
   - Visualizzazione contenuto in console

2. ELABORAZIONE - Metriche da calcolare
   - Conteggio caratteri (con e senza spazi)
   - Conteggio parole
   - Conteggio frasi
   - Conteggio paragrafi
   - Tempo di lettura stimato
   - Frequenza parole e lettere (ripetizioni)

3. OUTPUT - Destinazione risultati
   - Stampa in console
   - Scrittura su file

REGEX REFERENCE:
================

Pattern                 | Descrizione
------------------------|--------------------------------------------
.                       | Tutti i caratteri (con re.DOTALL include \n)
\S                      | Caratteri senza spazi
[a-zA-ZÀ-ÿ]             | Solo lettere (incluse accentate)
\w+                     | Parole (lettere, numeri, underscore)
[a-zA-ZÀ-ÿ]+            | Parole solo lettere (incluse accentate)
[^.!?]+[.!?]+           | Frasi (testo seguito da punteggiatura)
testo.split('\\n\\n')   | Paragrafi (separati da riga vuota)

# ===============================
#   Regex Patterns
# ===============================

REGEX_TUTTI_CARATTERI = r'.'           # Tutti i caratteri (usare con re.DOTALL)
REGEX_SENZA_SPAZI = r'\S'              # Caratteri esclusi gli spazi
REGEX_SOLO_LETTERE = r'[a-zA-ZÀ-ÿ]'   # Solo lettere, incluse accentate
REGEX_PAROLE = r'\w+'                  # Parole (lettere, numeri, underscore)
REGEX_PAROLE_LETTERE = r'[a-zA-ZÀ-ÿ]+' # Parole composte solo da lettere
REGEX_FRASI = r'[^.!?]+[.!?]+'         # Frasi terminate da . ! ?

"""

# ===============================
#   Repository
# =============================== 

from typing import TextIO

def get_file(file_path: str) -> TextIO:
    """Restituisce un oggetto TextIO con il contenuto del file specificato"""
    return open(file_path, "r")

# ===============================
#   Services
# =============================== 

def stampa_testo_input(text: TextIO) -> None:
    with text as f:
        content = f.read()
        print(content)

def get_testo(text: TextIO) -> str:
    with text as f:
        content = f.read()
        return content

def get_text_len(text: str) -> int:
    if text is None:
        print("La stringa vuota")
    print(len(text))

import re

def get_text_len_no_space(text: str) -> int:
    print(len(re.findall(r'\S', text)))

def main() -> None:
    try:
        content: TextIO = get_file("text.txt")
        get_text_len(get_testo(content))
        get_text_len_no_space(get_testo(content))
        
    except Exception as e:
        print(f"{e}")
    finally:
        print("fine try catch")


main()


        