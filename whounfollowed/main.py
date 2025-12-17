from requests import get
import re

"""
- Input 
- controllare che il nome inserito esista oppure no
  - se il nome esiste, continuiamo con lo scraping
  - se il nome non esiste, mostriamo un messaggio in cui diciamo che il profilo non esiste
"""


BASE_URL: int = "https://github.com" 
END_URL: str = "tab=followers" 

PATTERN = r'<a\s+[^>]*href="https://github\.com/([^/]+)\?page=(\d+)&amp;tab=followers"[^>]*>Next</a>'

def is_next_button_present(text: str) -> bool:
  if not text:
    raise ValueError("La stringa non puo essere vuota!")

  return bool(re.search(PATTERN, text))

def main() -> None:
  
  print("Start del programma")

  controller: bool = False

  # ==================
  # Primo while
  # ==================

  while True:

    try:
      nome_utente: str = input("Inserisci lo username del profilo github che vuoi analizzare:")

      if not nome_utente:
        raise ValueError("Il nome utente non può essere vuoto")
      
      # TODO: il nome exit esiste già come profilo  
      if nome_utente.strip().lower() == "exit":
        break

      print(f"Stai cercando: {nome_utente}")

      response = get(f"{BASE_URL}/{nome_utente}")

      if response.status_code == 404:
        print("Il profilo non esiste")
      else:
        print(f"Profilo {nome_utente} trovato")
        controller = True
        break 

    except Exception as e:
      print(f"OPS! Qualcosa è andato storto: {e}")
      
  # ==================
  # Secondo while
  # ==================

  counter: int = 1

  while controller:
    url = f"{BASE_URL}/{nome_utente}?page={counter}&{END_URL}"
    try:
      response = get(url)
      print(response.status_code)

      with open(f"tmp/pagina-{counter}.txt", "w") as f:
        f.write(response.text)
        controller = is_next_button_present(response.text)
        if controller:
          counter += 1 
        print("File salvato")


    except Exception as e:
      print(f"Errore: {e}") 

  print("Fine programma, arrivederci.")
 
if __name__ == "__main__":
  main()
