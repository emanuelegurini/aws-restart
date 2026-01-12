"""
Modulo per la gestione della persistenza dei dati in formato JSON.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    from models import ProjectDict, TaskDict, TagDict

DataDict = Dict[str, List[Any]]


DB_DIR = "db"
DB_FILE = os.path.join(DB_DIR, "db.json")


def ensure_db_exists() -> None:
    """
    Assicura che la cartella db e il file db.json esistano.
    Crea la struttura se non esiste.
    """
    os.makedirs(DB_DIR, exist_ok=True)
    
    if not os.path.exists(DB_FILE):
        initial_data = {
            "projects": [],
            "tasks": [],
            "tags": []
        }
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f, indent=2, ensure_ascii=False)


def load_data() -> DataDict:
    """
    Carica i dati dal file JSON.
    
    Returns:
        dict: Dizionario con projects, tasks e tags
    """
    ensure_db_exists()
    
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Assicurati che tutte le chiavi esistano
            if "projects" not in data:
                data["projects"] = []
            if "tasks" not in data:
                data["tasks"] = []
            if "tags" not in data:
                data["tags"] = []
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        # Se il file è corrotto o non esiste, crea una struttura vuota
        ensure_db_exists()
        initial_data = {
            "projects": [],
            "tasks": [],
            "tags": []
        }
        return initial_data


def save_data(data: DataDict) -> None:
    """
    Salva i dati nel file JSON.
    
    Args:
        data: Dizionario con projects, tasks e tags
    """
    ensure_db_exists()
    
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_projects() -> List[Dict[str, Any]]:
    """
    Ottiene la lista di tutti i progetti.
    
    Returns:
        list: Lista di progetti
    """
    data = load_data()
    return data.get("projects", [])


def get_tasks() -> List[Dict[str, Any]]:
    """
    Ottiene la lista di tutti i task.
    
    Returns:
        list: Lista di task
    """
    data = load_data()
    return data.get("tasks", [])


def get_tags() -> List[Dict[str, Any]]:
    """
    Ottiene la lista di tutti i tag.
    
    Returns:
        list: Lista di tag
    """
    data = load_data()
    return data.get("tags", [])


def save_projects(projects: List[Dict[str, Any]]) -> None:
    """
    Salva la lista dei progetti.
    
    Args:
        projects: Lista di progetti
    """
    data = load_data()
    data["projects"] = projects
    save_data(data)


def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    """
    Salva la lista dei task.
    
    Args:
        tasks: Lista di task
    """
    data = load_data()
    data["tasks"] = tasks
    save_data(data)


def save_tags(tags: List[Dict[str, Any]]) -> None:
    """
    Salva la lista dei tag.
    
    Args:
        tags: Lista di tag
    """
    data = load_data()
    data["tags"] = tags
    save_data(data)

