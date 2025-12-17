"""Entry point dell'applicazione"""

from ui.console import print_welcome_arcade, print_menu
from service import get_followers


def main() -> None:
    print_welcome_arcade()

    while True:
        print_menu()
        option = input("Inserisci qui la tua scelta: ").strip()

        match option:
            case "1":
                get_followers()
            case "2":
                print("Statistiche")  # TODO
            case "3":
                print("Dati per giorno")  # TODO
            case "exit":
                break
            case _:
                print("Opzione non valida. Riprova.")

    print("Fine programma, arrivederci.")


if __name__ == "__main__":
    main()
