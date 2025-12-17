"""Gestione persistenza dati su JSON"""

import json
import os


def check_if_json_db_has_correct_shape(db_name: str) -> bool:
    """Verifica che il db esiste ed è nella forma corretta."""
    if not os.path.isfile(db_name):
        return False

    with open(db_name, "r") as f:
        data = json.load(f)
        return isinstance(data, list)


def create_json_db(db_name: str) -> bool:
    """Crea un nuovo file db con lista vuota."""
    # Crea la cartella se non esiste
    os.makedirs(os.path.dirname(db_name), exist_ok=True)
    
    with open(db_name, "w") as f:
        f.write("[]")

    return True  # FIX: era "return bool"


def save_json_db(db_name: str, new_value: dict) -> None:
    """Salva il nuovo oggetto nel db."""
    if not check_if_json_db_has_correct_shape(db_name):
        create_json_db(db_name)

    db: list[dict] = []  # FIX: era list[str]

    with open(db_name, "r") as f:
        db.extend(json.load(f))

    db.append(new_value)

    with open(db_name, "w", encoding='utf-8') as f:
        json.dump(db, f, indent=4, ensure_ascii=False)