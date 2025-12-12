from requests import get, Response
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

BASE_URL: str = "https://api.escuelajs.co/api/v1/products"

# ===============================
#   Repository
# ===============================

def get_lista_prodotti(URL: str) -> list[dict[str, any]]:
    if URL is None: 
        raise ValueError("L'URL non può essere vuoto!")

    try: 
        response: Response = get_data(URL) 
        data = response.json()

        if not isinstance(data, list):
            raise TypeError(
                f"Risposta inattesa: mi aspettavo un lista, "
                f"ma ho ricevuto {type(data).__name__}"
        )

        return data
    except Exception as e:
        raise Exception(f"Problema con la response: {e}")

def get_prodotto(URL: str) -> dict[str, any]:
    if URL is None: 
        raise ValueError("L'URL non può essere vuoto!")

    try: 
        response: Response = get_data(URL) 
        data = response.json()

        if not isinstance(data, dict):
            raise TypeError(
                f"Risposta inattesa: mi aspettavo un dict, "
                f"ma ho ricevuto {type(data).__name__}"
        )

        return data

    except Exception as e:
        raise Exception(f"Problema con la response: {e}")

def get_data(URL: str) -> Response:
    if URL is None: 
        raise ValueError("L'URL non può essere vuoto!")
    
    try:
        response = get(URL)
        response.raise_for_status()
        return response

    except HTTPError as e:
        raise HTTPError(f"Errore HTTP {response.status_code} su {URL}: {response.reason}"
        ) from e

    except ConnectionError:
        raise ConnectionError(f"Impossibile connettersi a {URL}")
    
    except Timeout:
        raise Timeout(f"Timeout nella richiesta a {URL}")
    
    except RequestException as e:
        raise RequestException(f"Errore di rete imprevisto: {e}") from e

# ===============================
#   Model
# ===============================

def product_model(product: dict[str, any]) -> dict[str, any]:
    return {
        "id": product["id"], 
        "title": product["title"], 
        "price": product["price"], 
        "category": product["category"]["name"],
        "description": product["description"]
    }

def product_list_model(product_list: list[dict[str, any]]) -> list[dict[str, str]]:
    """Restituisce una lista di prodotti definita in {id: valore, title: nome prodotto}"""
    return [{"id": str(product["id"]), "title": str(product["title"])} for product in product_list]

# ===============================
#   UI
# ===============================

def print_prodotto(product: dict[str, any]) -> None:
    print("*" * 30)
    print("PRODOTTO")
    print("*" * 30)
    print(f"ID: {product["id"]}")
    print(f"Titolo: {product["title"]}")
    print(f"Category: {product["category"]}")
    print(f"PRICE: {product["price"]}")

def print_product_list(product_list: list[dict]) -> None:
    print("*" * 30)
    print("LISTA PRODOTTI")
    print("*" * 30)

    for product in product_list:
        print(f"{product["id"]} - {product["title"]}")


def main() -> None:

    try: 
        print_product_list(product_list_model(get_lista_prodotti(BASE_URL)))
        id = input("Inserisci l'id del prdotto da visualizzare:")
        product= product_model(get_prodotto(f"{BASE_URL}/{id}"))

        print_prodotto(product)
    
    except ValueError as e:
        print(f"{e}")
    
    except FileNotFoundError as e:
        print(f"{e}")
    
    except Exception as e:
        print(f"{e}") 

    

if __name__ == "__main__":
    main()