"""
mostra_menu() (senza return)
- Non prende parametri
- Stampa la domanda e le 4 opzioni
- Non restituisce nulla

raccogli_risposta() (con return)
- Non prende parametri
- Chiede l'input all'utente
- Restituisce la scelta


valida_scelta(scelta) (con return)
- prende come parametro il valore scelto
- Verifica se è A, B, C o D usando if
- Restituisce True se valida, False altrimenti

genera_feedback(scelta) (con return)
- Prende come parametro la lettera che è stata scelta
- Usa if/elif/else per determinare il messaggio
- Restituisce la stringa con il feedback personalizzato

"""

def genera_feedback(scelta: str) -> str:
    """
    Restituisce il messaggio che indica all'utente se ha indovinato la risposta oppure no.
    Questa funzione viene eseguita solo se la funzione di validazione restituisce true.
    """
    if scelta.upper() == "A": 
        return "Hai indovinato!"
    else:
        return "Non hai indovinato. Ritenta!"

def valida_scelta(scelta: str) -> bool:
    """
    Questa funzione prende un valore di tipo stringa e verifica che la risposta sia una delle opzioni tra A, B, C e D. 
    Se la risposta è una stringa vuota, restituisce false, idem se la risposta non è una di quelle sopra elencate.
    """
    scelta_tmp = scelta.upper()
    if scelta_tmp == "A" or scelta_tmp == "B" or scelta_tmp == "C" or scelta_tmp == "D":
        return True
    else: 
        return False

def mostra_domanda() -> None: 
    """
    Questa funzione restituisce la domanda e le opzioni della riposta. 
    """
    
    print(
"""
Chi parteciperà a Sanremo 2026?

A. Nayt
B. La Nina
C. Nilla Pizzi
D. Rocco Papaleo
"""
    )

def raccogli_risposta() -> str:
    """
    Questa funzione si occupa solamente di prendere l'input dell'utente. 
    Il controllo di tale valore avverrà attraverso una funzione dedicata.
    """ 
    return input("Inserisci la tua scelta: ")
    

mostra_domanda()
risposta_da_validare: str = raccogli_risposta()
risposta_validata: bool = valida_scelta(risposta_da_validare)
feedback: str = ""

if risposta_validata == True:
    feedback = genera_feedback(risposta_da_validare)
else: 
    feedback = "Inserisci solo la risposta tra le opzioni elencate"

print(feedback)