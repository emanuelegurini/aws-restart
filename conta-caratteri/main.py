# CONTACARATTERI

# DOMINIO:
# =========

# 1. INPUT - Sorgente del testo
#    - Lettura da file di testo (.txt)
#    - Visualizzazione contenuto in console

# 2. ELABORAZIONE - Metriche da calcolare
#   - Conteggio caratteri (con e senza spazi)
#   - Conteggio parole
#   - Conteggio frasi
#   - Conteggio paragrafi
#   - Tempo di lettura stimato
#   - Frequenza parole e lettere (ripetizioni)

# 3. OUTPUT - Destinazione risultati
#    - Stampa in console
#    - Scrittura su file

# REGEX REFERENCE:
# ================

# Pattern                 | Descrizione
# ------------------------|--------------------------------------------
# .                       | Tutti i caratteri (con re.DOTALL include \n)
# \S                      | Caratteri senza spazi
# [a-zA-ZÀ-ÿ]             | Solo lettere (incluse accentate)
# \w+                     | Parole (lettere, numeri, underscore)
# [a-zA-ZÀ-ÿ]+            | Parole solo lettere (incluse accentate)
# [^.!?]+[.!?]+           | Frasi (testo seguito da punteggiatura)
# testo.split('\\n\\n')   | Paragrafi (separati da riga vuota)

# ===============================
#   Regex Patterns
# ===============================

# REGEX_TUTTI_CARATTERI = r'.'           # Tutti i caratteri (usare con re.DOTALL)
# REGEX_SENZA_SPAZI = r'\S'              # Caratteri esclusi gli spazi
# REGEX_SOLO_LETTERE = r'[a-zA-ZÀ-ÿ]'   # Solo lettere, incluse accentate
# REGEX_PAROLE = r'\w+'                  # Parole (lettere, numeri, underscore)
# REGEX_PAROLE_LETTERE = r'[a-zA-ZÀ-ÿ]+' # Parole composte solo da lettere
# REGEX_FRASI = r'[^.!?]+[.!?]+'         # Frasi terminate da . ! ?


# ===============================
#   TODO 
# =============================== 

# 1. Migliorare gestione delle eccezzioni
# 2. Unificare gestione stream e buffer dati 
# 3. Suddividere in moduli

# ===============================
#   Repository
# =============================== 

from typing import TextIO

def get_file_content(file_path: str) -> str:
    if not file_path:
        raise ValueError("Il file path non può essere vuoto!")

    try:
        with open(file_path, "r") as f:
            return f.read()

    except FileNotFoundError:
        raise FileNotFoundError("Il file non esiste")

# ===============================
#   Services
# =============================== 

def stampa_testo_input(text: TextIO) -> None:
    with text as f:
        content = f.read()
        print(content)

import re

def get_text_len_no_space(text: str) -> int:
    print(len(re.findall(r'\S', text)))

def main() -> None:
    try:
        content: str = get_file_content("")
        print(content)

    except ValueError as e:
        print(f"{e}")
    
    except FileNotFoundError as e:
        print(f"{e}")
    
    except Exception as e:
        print(f"{e}")

    finally:
        print("fine try catch")


main()


        