"""Gestisce tutte le chiamate HTTP a GitHub"""

import re
from requests import get

from config import BASE_URL, END_URL, PATTERN_NEXT_BUTTON


def is_valid_username_format(username: str) -> bool:
    """Controlla che il formato sia accettabile per GitHub"""
    if not username or not username.strip():
        return False
    if username.strip().lower() == "exit":
        return False
    return bool(re.match(r'^[a-zA-Z0-9-]{1,39}$', username.strip()))


def check_user_exists(username: str) -> bool:
    """Verifica che il profilo esista su GitHub"""
    response = get(f"{BASE_URL}/{username.strip()}")
    return response.status_code != 404


def fetch_followers_page(username: str, page: int) -> str:
    """Scarica una singola pagina di follower, restituisce l'HTML"""
    url = f"{BASE_URL}/{username}?page={page}&{END_URL}"
    response = get(url)
    return response.text


def has_next_page(html: str) -> bool:
    """Controlla se c'è il pulsante Next nella pagina"""
    return bool(re.search(PATTERN_NEXT_BUTTON, html))