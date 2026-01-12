"""
Modulo per la creazione e validazione di progetti, task e tag.
Tutte le funzioni lavorano con dizionari, non classi.
"""
from __future__ import annotations

import uuid
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any

# Type aliases
ProjectDict = Dict[str, Any]
TaskDict = Dict[str, Any]
TagDict = Dict[str, Any]


def create_project(name: str, description: str = "") -> ProjectDict:
    """
    Crea un dizionario progetto.
    
    Args:
        name: Nome del progetto (univoco)
        description: Descrizione opzionale del progetto
    
    Returns:
        dict: Dizionario con i dati del progetto
    """
    return {
        "id": str(uuid.uuid4()),
        "name": name,
        "description": description,
        "created_at": datetime.now().isoformat()
    }


def create_task(
    title: str, project_id: str, tag_ids: Optional[List[str]] = None
) -> TaskDict:
    """
    Crea un dizionario task.
    
    Args:
        title: Titolo del task (univoco per progetto)
        project_id: ID del progetto a cui appartiene
        tag_ids: Lista di ID tag (opzionale)
    
    Returns:
        dict: Dizionario con i dati del task
    """
    if tag_ids is None:
        tag_ids = []
    
    return {
        "id": str(uuid.uuid4()),
        "title": title,
        "completed": False,
        "project_id": project_id,
        "tag_ids": tag_ids,
        "created_at": datetime.now().isoformat(),
        "completed_at": None
    }


def create_tag(name: str, color: str = "") -> TagDict:
    """
    Crea un dizionario tag.
    
    Args:
        name: Nome del tag (univoco)
        color: Colore opzionale del tag
    
    Returns:
        dict: Dizionario con i dati del tag
    """
    return {
        "id": str(uuid.uuid4()),
        "name": name,
        "color": color
    }


def validate_project_name(
    name: str, existing_projects: List[ProjectDict]
) -> Tuple[bool, Optional[str]]:
    """
    Valida che il nome del progetto sia univoco.
    
    Args:
        name: Nome da validare
        existing_projects: Lista di progetti esistenti
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if not name or not name.strip():
        return False, "Il nome del progetto non può essere vuoto"
    
    for project in existing_projects:
        if project["name"].lower() == name.lower():
            return False, f"Un progetto con il nome '{name}' esiste già"
    
    return True, None


def validate_task_title(
    title: str, project_id: str, existing_tasks: List[TaskDict]
) -> Tuple[bool, Optional[str]]:
    if not title or not title.strip():
        return False, "Il titolo del task non può essere vuoto"
    
    for task in existing_tasks:
        if (task["project_id"] == project_id and 
            task["title"].lower() == title.lower()):
            return False, f"Un task con il titolo '{title}' esiste già in questo progetto"
    
    return True, None


def validate_tag_name(
    name: str, existing_tags: List[TagDict]
) -> Tuple[bool, Optional[str]]:
    if not name or not name.strip():
        return False, "Il nome del tag non può essere vuoto"
    
    for tag in existing_tags:
        if tag["name"].lower() == name.lower():
            return False, f"Un tag con il nome '{name}' esiste già"
    
    return True, None


def validate_tag_color(color: str) -> Tuple[bool, Optional[str]]:
    valid_colors = ["red", "blue", "green", "yellow", "magenta", "cyan", "white"]
    
    if color and color.lower() not in valid_colors:
        return False, f"Colore non valido. Colori disponibili: {', '.join(valid_colors)}"
    
    return True, None


def find_project_by_id(
    project_id: str, projects: List[ProjectDict]
) -> Optional[ProjectDict]:
    for project in projects:
        if project["id"] == project_id:
            return project
    return None


def find_project_by_name(
    name: str, projects: List[ProjectDict]
) -> Optional[ProjectDict]:
    """
    Trova un progetto per nome.
    
    Args:
        name: Nome del progetto
        projects: Lista di progetti
    
    Returns:
        dict o None: Il progetto trovato o None
    """
    for project in projects:
        if project["name"].lower() == name.lower():
            return project
    return None


def find_task_by_id(task_id: str, tasks: List[TaskDict]) -> Optional[TaskDict]:
    """
    Trova un task per ID.
    
    Args:
        task_id: ID del task
        tasks: Lista di task
    
    Returns:
        dict o None: Il task trovato o None
    """
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def find_tag_by_id(tag_id: str, tags: List[TagDict]) -> Optional[TagDict]:
    """
    Trova un tag per ID.
    
    Args:
        tag_id: ID del tag
        tags: Lista di tag
    
    Returns:
        dict o None: Il tag trovato o None
    """
    for tag in tags:
        if tag["id"] == tag_id:
            return tag
    return None


def find_tag_by_name(name: str, tags: List[TagDict]) -> Optional[TagDict]:
    """
    Trova un tag per nome.
    
    Args:
        name: Nome del tag
        tags: Lista di tag
    
    Returns:
        dict o None: Il tag trovato o None
    """
    for tag in tags:
        if tag["name"].lower() == name.lower():
            return tag
    return None

