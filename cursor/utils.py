"""
Modulo con funzioni di utilità per formattazione output, validazione e visualizzazione.
"""
from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional

from models import ProjectDict, TagDict, TaskDict


# Codici ANSI per i colori
COLORS: Dict[str, str] = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "reset": "\033[0m"
}


def format_date(date_str: Optional[str]) -> str:
    """
    Formatta una data ISO in formato leggibile.
    
    Args:
        date_str: Stringa data in formato ISO
    
    Returns:
        str: Data formattata o stringa vuota se None
    """
    if not date_str:
        return ""
    
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%Y-%m-%d %H:%M")
    except (ValueError, TypeError):
        return date_str


def format_task_status(completed: bool) -> str:
    """
    Formatta lo stato del task con emoji.
    
    Args:
        completed: True se completato, False altrimenti
    
    Returns:
        str: Emoji che rappresenta lo stato
    """
    return "✓" if completed else "○"


def format_tag_color(tag: TagDict) -> str:
    """
    Formatta un tag con il suo colore se disponibile.
    
    Args:
        tag: Dizionario tag
    
    Returns:
        str: Tag formattato con colore ANSI
    """
    name = tag.get("name", "")
    color = tag.get("color", "").lower()
    
    if color and color in COLORS:
        return f"{COLORS[color]}{name}{COLORS['reset']}"
    
    return name


def print_success(message: str) -> None:
    """
    Stampa un messaggio di successo.
    
    Args:
        message: Messaggio da stampare
    """
    print(f"{COLORS['green']}✓ {message}{COLORS['reset']}")


def print_error(message: str) -> None:
    """
    Stampa un messaggio di errore.
    
    Args:
        message: Messaggio da stampare
    """
    print(f"{COLORS['red']}✗ Errore: {message}{COLORS['reset']}")


def print_info(message: str) -> None:
    """
    Stampa un messaggio informativo.
    
    Args:
        message: Messaggio da stampare
    """
    print(f"{COLORS['blue']}ℹ {message}{COLORS['reset']}")


def print_projects(projects: List[ProjectDict]) -> None:
    """
    Stampa la lista dei progetti in formato tabellare.
    
    Args:
        projects: Lista di progetti
    """
    if not projects:
        print_info("Nessun progetto trovato.")
        return
    
    print("\n" + "=" * 80)
    print(f"{'ID':<36} {'Nome':<30} {'Creato il':<20}")
    print("=" * 80)
    
    for project in projects:
        created = format_date(project.get("created_at", ""))
        desc = project.get("description", "")
        print(f"{project['id']:<36} {project['name']:<30} {created:<20}")
        if desc:
            print(f"  Descrizione: {desc}")
    
    print("=" * 80 + "\n")


def print_tasks(
    tasks: List[TaskDict],
    projects: Optional[List[ProjectDict]] = None,
    tags: Optional[List[TagDict]] = None,
) -> None:
    """
    Stampa la lista dei task in formato tabellare.
    
    Args:
        tasks: Lista di task
        projects: Lista di progetti (opzionale, per mostrare il nome del progetto)
        tags: Lista di tag (opzionale, per mostrare i nomi dei tag)
    """
    if not tasks:
        print_info("Nessun task trovato.")
        return
    
    # Crea dizionari per lookup veloce
    project_dict = {}
    if projects:
        project_dict = {p["id"]: p["name"] for p in projects}
    
    tag_dict = {}
    if tags:
        tag_dict = {t["id"]: t for t in tags}
    
    print("\n" + "=" * 100)
    print(f"{'Stato':<4} {'Titolo':<30} {'Progetto':<20} {'Tag':<30} {'Creato il':<15}")
    print("=" * 100)
    
    for task in tasks:
        status = format_task_status(task.get("completed", False))
        title = task.get("title", "")
        project_id = task.get("project_id", "")
        project_name = project_dict.get(project_id, project_id[:8] + "...")
        
        # Formatta i tag
        tag_ids = task.get("tag_ids", [])
        tag_names = []
        for tag_id in tag_ids:
            tag = tag_dict.get(tag_id)
            if tag:
                tag_names.append(format_tag_color(tag))
        
        tags_str = ", ".join(tag_names) if tag_names else "-"
        created = format_date(task.get("created_at", ""))
        
        print(f"{status:<4} {title:<30} {project_name:<20} {tags_str:<30} {created:<15}")
        
        if task.get("completed_at"):
            completed = format_date(task.get("completed_at", ""))
            print(f"     Completato il: {completed}")
    
    print("=" * 100 + "\n")


def print_tags(tags: List[TagDict]) -> None:
    """
    Stampa la lista dei tag in formato tabellare.
    
    Args:
        tags: Lista di tag
    """
    if not tags:
        print_info("Nessun tag trovato.")
        return
    
    print("\n" + "=" * 80)
    print(f"{'ID':<36} {'Nome':<30} {'Colore':<15}")
    print("=" * 80)
    
    for tag in tags:
        name = format_tag_color(tag)
        color = tag.get("color", "-")
        print(f"{tag['id']:<36} {name:<30} {color:<15}")
    
    print("=" * 80 + "\n")


def get_input(prompt: str, default: str = "") -> str:
    """
    Ottiene input dall'utente con un prompt.
    
    Args:
        prompt: Messaggio da mostrare
        default: Valore di default se l'utente non inserisce nulla
    
    Returns:
        str: Input dell'utente o valore di default
    """
    if default:
        user_input = input(f"{prompt} [{default}]: ").strip()
        return user_input if user_input else default
    else:
        return input(f"{prompt}: ").strip()


def get_yes_no(prompt: str, default: bool = True) -> bool:
    """
    Ottiene una risposta sì/no dall'utente.
    
    Args:
        prompt: Messaggio da mostrare
        default: Valore di default (True per sì, False per no)
    
    Returns:
        bool: True per sì, False per no
    """
    default_str = "S/n" if default else "s/N"
    response = input(f"{prompt} [{default_str}]: ").strip().lower()
    
    if not response:
        return default
    
    return response in ["s", "si", "sì", "y", "yes"]

