def mostra_feedback(messaggio: str) -> None:
    """
    Restituisce il feedback formattato nella maniera desiderata.
    """
    simbol: str = "*"*30
    print(f"""
{simbol}
{messaggio}
{simbol}
""")

def mostra_domanda(domanda: str) -> None: 
    """
    Questa funzione restituisce la domanda e le opzioni della riposta. 
    """
    
    print(domanda)

def print_numero_domanda(valore_domanda_corrente: int, valore_domande_totali: int) -> None:
    """Restituisce l'indicatore della domanda corrente rispetto al numero di domande totali"""
    print("------------------------------")
    print(f"Domanda {valore_domanda_corrente} di {valore_domande_totali}")
    print("------------------------------")


def print_gioco_terminato() -> None:
    print("*"*30)
    print("Gioco terminato. Ecco i risultati:")
    print("*"*30)
