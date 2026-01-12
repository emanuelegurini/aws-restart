"""
Todo List CLI - Entry point principale con menu interattivo.
"""
from __future__ import annotations

import sys
from datetime import datetime

from models import (
    create_project,
    create_task,
    create_tag,
    find_project_by_id,
    find_project_by_name,
    find_tag_by_id,
    find_tag_by_name,
    find_task_by_id,
    validate_project_name,
    validate_tag_color,
    validate_tag_name,
    validate_task_title,
)
from storage import (
    get_projects,
    get_tags,
    get_tasks,
    save_projects,
    save_tags,
    save_tasks,
)
from utils import (
    format_date,
    get_input,
    get_yes_no,
    print_error,
    print_info,
    print_projects,
    print_success,
    print_tags,
    print_tasks,
)


# ============================================================================
# FUNZIONALITÀ PROGETTI
# ============================================================================

def create_project_handler() -> None:
    """Gestisce la creazione di un nuovo progetto."""
    print("\n--- Crea Nuovo Progetto ---")
    
    name = get_input("Nome del progetto")
    if not name:
        print_error("Il nome del progetto è obbligatorio.")
        return
    
    projects = get_projects()
    is_valid, error_msg = validate_project_name(name, projects)
    if not is_valid:
        print_error(error_msg)
        return
    
    description = get_input("Descrizione (opzionale)", "")
    
    new_project = create_project(name, description)
    projects.append(new_project)
    save_projects(projects)
    
    print_success(f"Progetto '{name}' creato con successo!")


def list_projects_handler() -> None:
    """Gestisce la visualizzazione di tutti i progetti."""
    print("\n--- Lista Progetti ---")
    projects = get_projects()
    print_projects(projects)


def delete_project_handler() -> None:
    """Gestisce l'eliminazione di un progetto e dei suoi task."""
    print("\n--- Elimina Progetto ---")
    
    projects = get_projects()
    if not projects:
        print_error("Nessun progetto disponibile.")
        return
    
    print_projects(projects)
    project_name = get_input("Nome del progetto da eliminare")
    
    if not project_name:
        print_error("Nome progetto non valido.")
        return
    
    project = find_project_by_name(project_name, projects)
    if not project:
        print_error(f"Progetto '{project_name}' non trovato.")
        return
    
    # Rimuovi tutti i task associati
    tasks = get_tasks()
    tasks = [t for t in tasks if t["project_id"] != project["id"]]
    save_tasks(tasks)
    
    # Rimuovi il progetto
    projects = [p for p in projects if p["id"] != project["id"]]
    save_projects(projects)
    
    print_success(f"Progetto '{project_name}' e tutti i suoi task sono stati eliminati.")


# ============================================================================
# FUNZIONALITÀ TASK
# ============================================================================

def create_task_handler() -> None:
    """Gestisce la creazione di un nuovo task."""
    print("\n--- Crea Nuovo Task ---")
    
    projects = get_projects()
    if not projects:
        print_error("Nessun progetto disponibile. Crea prima un progetto.")
        return
    
    print_projects(projects)
    project_name = get_input("Nome del progetto")
    
    if not project_name:
        print_error("Nome progetto non valido.")
        return
    
    project = find_project_by_name(project_name, projects)
    if not project:
        print_error(f"Progetto '{project_name}' non trovato.")
        return
    
    title = get_input("Titolo del task")
    if not title:
        print_error("Il titolo del task è obbligatorio.")
        return
    
    tasks = get_tasks()
    is_valid, error_msg = validate_task_title(title, project["id"], tasks)
    if not is_valid:
        print_error(error_msg)
        return
    
    new_task = create_task(title, project["id"])
    tasks.append(new_task)
    save_tasks(tasks)
    
    print_success(f"Task '{title}' creato con successo!")


def list_tasks_handler() -> None:
    """Gestisce la visualizzazione dei task."""
    print("\n--- Lista Task ---")
    
    tasks = get_tasks()
    projects = get_projects()
    tags = get_tags()
    
    if not tasks:
        print_info("Nessun task trovato.")
        return
    
    # Chiedi se filtrare
    filter_choice = get_input("Filtrare per (progetto/tag/niente)", "niente").lower()
    
    if filter_choice == "progetto":
        print_projects(projects)
        project_name = get_input("Nome del progetto")
        if project_name:
            project = find_project_by_name(project_name, projects)
            if project:
                tasks = [t for t in tasks if t["project_id"] == project["id"]]
            else:
                print_error(f"Progetto '{project_name}' non trovato.")
                return
    
    elif filter_choice == "tag":
        print_tags(tags)
        tag_name = get_input("Nome del tag")
        if tag_name:
            tag = find_tag_by_name(tag_name, tags)
            if tag:
                tasks = [t for t in tasks if tag["id"] in t.get("tag_ids", [])]
            else:
                print_error(f"Tag '{tag_name}' non trovato.")
                return
    
    print_tasks(tasks, projects, tags)


def toggle_task_completion_handler() -> None:
    """Gestisce il completamento/riapertura di un task."""
    print("\n--- Segna Task Completato/Riapri ---")
    
    tasks = get_tasks()
    if not tasks:
        print_error("Nessun task disponibile.")
        return
    
    projects = get_projects()
    tags = get_tags()
    print_tasks(tasks, projects, tags)
    
    task_title = get_input("Titolo del task")
    if not task_title:
        print_error("Titolo task non valido.")
        return
    
    # Trova il task (potrebbe esserci più di uno con lo stesso titolo in progetti diversi)
    matching_tasks = [t for t in tasks if t["title"].lower() == task_title.lower()]
    
    if not matching_tasks:
        print_error(f"Task '{task_title}' non trovato.")
        return
    
    if len(matching_tasks) > 1:
        print_info("Trovati più task con questo titolo:")
        for i, task in enumerate(matching_tasks, 1):
            project = find_project_by_id(task["project_id"], projects)
            project_name = project["name"] if project else "Sconosciuto"
            status = "Completato" if task.get("completed") else "Aperto"
            print(f"  {i}. {task['title']} - Progetto: {project_name} - {status}")
        
        choice = get_input("Numero del task da modificare")
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(matching_tasks):
                task = matching_tasks[idx]
            else:
                print_error("Scelta non valida.")
                return
        except ValueError:
            print_error("Numero non valido.")
            return
    else:
        task = matching_tasks[0]
    
    # Toggle completamento
    task["completed"] = not task.get("completed", False)
    if task["completed"]:
        task["completed_at"] = datetime.now().isoformat()
    else:
        task["completed_at"] = None
    
    # Aggiorna la lista
    for i, t in enumerate(tasks):
        if t["id"] == task["id"]:
            tasks[i] = task
            break
    
    save_tasks(tasks)
    
    status = "completato" if task["completed"] else "riaperto"
    print_success(f"Task '{task['title']}' {status} con successo!")


def assign_tags_to_task_handler() -> None:
    """Gestisce l'assegnazione di tag a un task."""
    print("\n--- Assegna Tag a Task ---")
    
    tasks = get_tasks()
    if not tasks:
        print_error("Nessun task disponibile.")
        return
    
    projects = get_projects()
    tags = get_tags()
    print_tasks(tasks, projects, tags)
    
    task_title = get_input("Titolo del task")
    if not task_title:
        print_error("Titolo task non valido.")
        return
    
    matching_tasks = [t for t in tasks if t["title"].lower() == task_title.lower()]
    
    if not matching_tasks:
        print_error(f"Task '{task_title}' non trovato.")
        return
    
    if len(matching_tasks) > 1:
        print_info("Trovati più task con questo titolo:")
        for i, task in enumerate(matching_tasks, 1):
            project = find_project_by_id(task["project_id"], projects)
            project_name = project["name"] if project else "Sconosciuto"
            print(f"  {i}. {task['title']} - Progetto: {project_name}")
        
        choice = get_input("Numero del task da modificare")
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(matching_tasks):
                task = matching_tasks[idx]
            else:
                print_error("Scelta non valida.")
                return
        except ValueError:
            print_error("Numero non valido.")
            return
    else:
        task = matching_tasks[0]
    
    if not tags:
        print_error("Nessun tag disponibile. Crea prima un tag.")
        return
    
    print_tags(tags)
    tag_names_input = get_input("Nomi dei tag (separati da virgola)")
    
    if not tag_names_input:
        print_error("Nessun tag specificato.")
        return
    
    tag_names = [name.strip() for name in tag_names_input.split(",")]
    tag_ids = []
    
    for tag_name in tag_names:
        tag = find_tag_by_name(tag_name, tags)
        if tag:
            tag_ids.append(tag["id"])
        else:
            print_error(f"Tag '{tag_name}' non trovato.")
            return
    
    # Aggiorna i tag del task
    task["tag_ids"] = list(set(tag_ids))  # Rimuovi duplicati
    
    # Aggiorna la lista
    for i, t in enumerate(tasks):
        if t["id"] == task["id"]:
            tasks[i] = task
            break
    
    save_tasks(tasks)
    
    print_success(f"Tag assegnati al task '{task['title']}' con successo!")


def delete_task_handler() -> None:
    """Gestisce l'eliminazione di un task."""
    print("\n--- Elimina Task ---")
    
    tasks = get_tasks()
    if not tasks:
        print_error("Nessun task disponibile.")
        return
    
    projects = get_projects()
    tags = get_tags()
    print_tasks(tasks, projects, tags)
    
    task_title = get_input("Titolo del task da eliminare")
    if not task_title:
        print_error("Titolo task non valido.")
        return
    
    matching_tasks = [t for t in tasks if t["title"].lower() == task_title.lower()]
    
    if not matching_tasks:
        print_error(f"Task '{task_title}' non trovato.")
        return
    
    if len(matching_tasks) > 1:
        print_info("Trovati più task con questo titolo:")
        for i, task in enumerate(matching_tasks, 1):
            project = find_project_by_id(task["project_id"], projects)
            project_name = project["name"] if project else "Sconosciuto"
            print(f"  {i}. {task['title']} - Progetto: {project_name}")
        
        choice = get_input("Numero del task da eliminare")
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(matching_tasks):
                task = matching_tasks[idx]
            else:
                print_error("Scelta non valida.")
                return
        except ValueError:
            print_error("Numero non valido.")
            return
    else:
        task = matching_tasks[0]
    
    if not get_yes_no(f"Sei sicuro di voler eliminare il task '{task['title']}'?", False):
        print_info("Operazione annullata.")
        return
    
    tasks = [t for t in tasks if t["id"] != task["id"]]
    save_tasks(tasks)
    
    print_success(f"Task '{task['title']}' eliminato con successo!")


# ============================================================================
# FUNZIONALITÀ TAG
# ============================================================================

def create_tag_handler() -> None:
    """Gestisce la creazione di un nuovo tag."""
    print("\n--- Crea Nuovo Tag ---")
    
    name = get_input("Nome del tag")
    if not name:
        print_error("Il nome del tag è obbligatorio.")
        return
    
    tags = get_tags()
    is_valid, error_msg = validate_tag_name(name, tags)
    if not is_valid:
        print_error(error_msg)
        return
    
    color = get_input("Colore (red, blue, green, yellow, magenta, cyan, white) - opzionale", "")
    
    if color:
        is_valid, error_msg = validate_tag_color(color)
        if not is_valid:
            print_error(error_msg)
            return
    
    new_tag = create_tag(name, color)
    tags.append(new_tag)
    save_tags(tags)
    
    print_success(f"Tag '{name}' creato con successo!")


def list_tags_handler() -> None:
    """Gestisce la visualizzazione di tutti i tag."""
    print("\n--- Lista Tag ---")
    tags = get_tags()
    print_tags(tags)


def delete_tag_handler() -> None:
    """Gestisce l'eliminazione di un tag (lo rimuove anche dai task)."""
    print("\n--- Elimina Tag ---")
    
    tags = get_tags()
    if not tags:
        print_error("Nessun tag disponibile.")
        return
    
    print_tags(tags)
    tag_name = get_input("Nome del tag da eliminare")
    
    if not tag_name:
        print_error("Nome tag non valido.")
        return
    
    tag = find_tag_by_name(tag_name, tags)
    if not tag:
        print_error(f"Tag '{tag_name}' non trovato.")
        return
    
    # Rimuovi il tag da tutti i task
    tasks = get_tasks()
    for task in tasks:
        if tag["id"] in task.get("tag_ids", []):
            task["tag_ids"] = [tid for tid in task["tag_ids"] if tid != tag["id"]]
    save_tasks(tasks)
    
    # Rimuovi il tag
    tags = [t for t in tags if t["id"] != tag["id"]]
    save_tags(tags)
    
    print_success(f"Tag '{tag_name}' eliminato e rimosso da tutti i task.")


# ============================================================================
# MENU PRINCIPALE
# ============================================================================

def show_projects_menu() -> None:
    """Mostra il menu dei progetti."""
    while True:
        print("\n" + "=" * 50)
        print("GESTIONE PROGETTI")
        print("=" * 50)
        print("1. Crea nuovo progetto")
        print("2. Lista progetti")
        print("3. Elimina progetto")
        print("0. Torna al menu principale")
        
        choice = get_input("\nScelta")
        
        if choice == "1":
            create_project_handler()
        elif choice == "2":
            list_projects_handler()
        elif choice == "3":
            delete_project_handler()
        elif choice == "0":
            break
        else:
            print_error("Scelta non valida.")


def show_tasks_menu() -> None:
    """Mostra il menu dei task."""
    while True:
        print("\n" + "=" * 50)
        print("GESTIONE TASK")
        print("=" * 50)
        print("1. Crea nuovo task")
        print("2. Lista task")
        print("3. Segna completato/riapri")
        print("4. Assegna tag a task")
        print("5. Elimina task")
        print("0. Torna al menu principale")
        
        choice = get_input("\nScelta")
        
        if choice == "1":
            create_task_handler()
        elif choice == "2":
            list_tasks_handler()
        elif choice == "3":
            toggle_task_completion_handler()
        elif choice == "4":
            assign_tags_to_task_handler()
        elif choice == "5":
            delete_task_handler()
        elif choice == "0":
            break
        else:
            print_error("Scelta non valida.")


def show_tags_menu() -> None:
    """Mostra il menu dei tag."""
    while True:
        print("\n" + "=" * 50)
        print("GESTIONE TAG")
        print("=" * 50)
        print("1. Crea nuovo tag")
        print("2. Lista tag")
        print("3. Elimina tag")
        print("0. Torna al menu principale")
        
        choice = get_input("\nScelta")
        
        if choice == "1":
            create_tag_handler()
        elif choice == "2":
            list_tags_handler()
        elif choice == "3":
            delete_tag_handler()
        elif choice == "0":
            break
        else:
            print_error("Scelta non valida.")


def main() -> None:
    """Funzione principale con menu interattivo."""
    print("\n" + "=" * 50)
    print("TODO LIST CLI")
    print("=" * 50)
    
    while True:
        print("\nMENU PRINCIPALE")
        print("1. Progetti")
        print("2. Task")
        print("3. Tag")
        print("0. Esci")
        
        choice = get_input("\nScelta")
        
        if choice == "1":
            show_projects_menu()
        elif choice == "2":
            show_tasks_menu()
        elif choice == "3":
            show_tags_menu()
        elif choice == "0":
            print_info("Arrivederci!")
            break
        else:
            print_error("Scelta non valida.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nArrivederci!")
        sys.exit(0)

