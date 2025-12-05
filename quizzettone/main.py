from data.services import (
    get_domanda_e_risposta_singola, 
    get_lista_domande_e_risposte, 
    estrai_indice_simbolo, 
    estrai_domanda, 
    estrai_risposta, 
    valida_scelta, 
    is_risposta_esatta, 
    get_numero_domanda_corrente, 
    get_counter_aggiornato,
    genera_statistiche,
    calcola_percentuale,
    verifica_superamento
)
from ui.console import (
    mostra_feedback, 
    mostra_domanda, 
    print_numero_domanda, 
    print_gioco_terminato, 
    genera_feedback, 
    raccogli_risposta,
    mostra_riepilogo,
    mostra_risultati_finali
)


def main():

    lista_domande = get_lista_domande_e_risposte("domande.txt")
    risultato_finale: list[dict[str, str | bool]] = []
    domanda_e_risposta: dict[str, str] = {"domanda" : None, "risposta" : None}

    counter_domanda_corrente: int = 0
    lista_domande_length: int = len(lista_domande)

    while counter_domanda_corrente <= lista_domande_length:

        # oltre l'ultima domanda, chiediamo se proseguire
        if counter_domanda_corrente == lista_domande_length:
            mostra_riepilogo(risultato_finale)
        
            scelta = input("\nInserisci il numero della domanda da rivedere o premi INVIO per terminare: ")
            
            if scelta == "":
                break 
            elif scelta.isdigit():
                numero = int(scelta)
                if 1 <= numero <= lista_domande_length:
                    counter_domanda_corrente = numero - 1
                    print(f"Torna alla domanda {numero}...")
                    continue 
                else:
                    print("Numero non valido.")
            else:
                print("Input non valido.")
        
        # recupero dei dati
        content: str = get_domanda_e_risposta_singola(f"domande_risposte/{lista_domande[counter_domanda_corrente]}")
        index: int = estrai_indice_simbolo(content)
        domanda_e_risposta["domanda"] = estrai_domanda(content, index)
        domanda_e_risposta["risposta"] = estrai_risposta(content, index)

        # presentazione domande
        domanda_corrente: int = get_numero_domanda_corrente(counter_domanda_corrente)
        print_numero_domanda(domanda_corrente, lista_domande_length)
        mostra_domanda(domanda_e_risposta["domanda"])

        # input dell'utente
        risposta_utente: str = raccogli_risposta()
        is_risposta_valid: bool = valida_scelta(risposta_utente)

        feedback: str = ""

        if is_risposta_valid:
            risultato: dict[str, str | bool] = {}
            is_risposta_corretta: bool = is_risposta_esatta(risposta_utente, domanda_e_risposta["risposta"])

            feedback = genera_feedback(is_risposta_corretta)

            risultato["domanda"] = lista_domande[counter_domanda_corrente]
            risultato["risposta_corretta"] = is_risposta_corretta

            risultato["scelta_utente"] = risposta_utente.upper()

            # gestione della lista risultati
            if counter_domanda_corrente < len(risultato_finale):
                risultato_finale[counter_domanda_corrente] = risultato
            else:
                risultato_finale.append(risultato)

        else: 
            feedback = "Inserisci solo la risposta tra le opzioni elencate"

        mostra_feedback(feedback)
        
        # navigazione domanda (successiva / precedente)
        if counter_domanda_corrente > 0:
            input_prev_next: str = input("Digita 'P' per andare alla domanda precedente oppure qualsiasi altro tasto per continuare: ")
            counter_domanda_corrente = get_counter_aggiornato(counter_domanda_corrente, input_prev_next)
        else:
            counter_domanda_corrente += 1 


    statistiche: dict[str, int] = genera_statistiche(risultato_finale)
    
    print_gioco_terminato()

    statistiche = genera_statistiche(risultato_finale)
    esatte = statistiche["risposte_esatte"]
    errate = statistiche["risposte_non_esatte"]
    totale_domande_fatte = esatte + errate
    
    perc = calcola_percentuale(esatte, totale_domande_fatte)
    is_superato = verifica_superamento(perc)
    
    mostra_risultati_finali(esatte, errate, totale_domande_fatte, perc, is_superato)

if __name__ == "__main__": 
    main()