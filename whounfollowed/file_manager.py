"""Gestisce lettura/scrittura file temporanei e parsing"""

import os
import re
import shutil

from config import TMP_DIR, PATTERN_USER


def ensure_tmp_dir_exists() -> None:
    """Crea la cartella tmp se non esiste"""
    if not os.path.exists(TMP_DIR):
        os.makedirs(TMP_DIR)


def clear_tmp_dir() -> None:
    """Svuota la cartella tmp"""
    if os.path.exists(TMP_DIR):
        shutil.rmtree(TMP_DIR)
    os.makedirs(TMP_DIR)


def save_page(page_number: int, content: str) -> None:
    """Salva una pagina HTML nel file temporaneo"""
    filepath = f"{TMP_DIR}/pagina-{page_number}.txt"
    with open(filepath, "w") as f:
        f.write(content)


def read_page(page_number: int) -> str:
    """Legge una pagina dal file temporaneo"""
    filepath = f"{TMP_DIR}/pagina-{page_number}.txt"
    with open(filepath, "r") as f:
        return f.read()


def extract_usernames_from_page(html: str) -> list[str]:
    """Estrae gli username da una pagina HTML"""
    return re.findall(PATTERN_USER, html)


def extract_all_usernames(page_count: int) -> list[str]:
    """Estrae tutti gli username da tutte le pagine salvate"""
    usernames: list[str] = []
    for i in range(1, page_count + 1):
        html = read_page(i)
        usernames.extend(extract_usernames_from_page(html))
    return usernames