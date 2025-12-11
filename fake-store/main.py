from requests import get, exceptions

BASE_URL: str = "https://api.escuelajs.co/api/v1/products"

def get_data(URL: str) -> dict[str, any] | list[dict[str, any]]:
    if URL is None: 
        raise ValueError("L'URL non può essere vuoto!")
    
    try:
        response = get(URL)
        response.raise_for_status()
        return response.json()

    except exceptions.HTTPError:
        # TODO: correggere exceptions
        raise exceptions.HTTPError("errore")


def print_prodotto(product: dict[str, any]) -> None:
    print("*" * 30)
    print(f"PRODOTTO")
    print("*" * 30)
    print(f"ID: {product["id"]}")
    print(f"Titolo: {product["title"]}")
    print(f"Category: {product["category"]}")
    print(f"PRICE: {product["price"]}")
    print(f"DESCRIPTION: {product["description"]}")


def product_model(product: dict[str, any]) -> dict[str, any]:
    return {
        "id": product["id"], 
        "title": product["title"], 
        "price": product["price"], 
        "category": product["category"]["name"],
        "description": product["description"]
    }
    

def main() -> None:

    try: 
        id = input("Inserisci l'id del prdotto da visualizzare:")
        product= product_model(get_data(f"{BASE_URL}/{id}"))
        print_prodotto(product)
    
    except Exception as e:
        print(f"Errore: {e}")

    

if __name__ == "__main__":
    main()