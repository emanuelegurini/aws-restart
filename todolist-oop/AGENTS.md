# AGENTS.md

This document provides guidance for agentic coding assistants working in this repository.

## Build, Lint, Test Commands

### Linting
- Run linter: `ruff check .`
- Auto-fix linting issues: `ruff check . --fix`

### Running the Application
- Execute the main application: `python3 main.py`

### Testing
- No test framework is currently configured. Tests should be added using pytest.

## Code Style Guidelines

### General
- Python 3.14.2 is the target version
- Use ruff for code linting and formatting
- All code must pass ruff checks before committing

### Naming Conventions
- **Classes**: PascalCase (e.g., `Project`, `Task`, `Todolist`)
- **Functions/Methods**: snake_case (e.g., `get_project_id`, `add_new_task`)
- **Variables**: snake_case (e.g., `project_name`, `task_list`)
- **Constants**: UPPER_SNAKE_CASE (not currently used, but adopt if needed)
- **Private methods**: prefix with underscore (e.g., `_internal_method`)

### Type Hints
- Always include type hints for function signatures
- Use Python's built-in type hints: `list[Type]`, `dict[KeyType, ValueType]`
- Use Union types with `|` operator: `Type | None` instead of `Optional[Type]`
- Method return types should be explicit: `-> str`, `-> None`, `-> Project | None`

### Imports
- Import standard library modules first
- Import third-party packages second
- Import local modules last
- Each import on its own line
- Avoid wildcard imports (`from module import *`)
- Group imports by type with blank lines between groups

```python
# Standard library
import uuid

# Local modules
from project import Project
from task import Task
```

### Formatting
- 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters (ruff default)
- One statement per line (avoid `case "1": func()` on one line)
- Blank line between top-level definitions
- Two blank lines before class definitions, one before method definitions

### Documentation
- Use docstrings for all classes, methods, and functions
- Docstrings should be triple-quoted strings
- Keep docstrings concise and descriptive
- Examples:

```python
def get_project_name(self) -> str:
    """Return the project name."""
    return self.name

def set_project_name(self, new_name: str) -> None:
    """Set the project name (useful for updates)."""
    self.name = new_name
```

### Error Handling
- Validate input types with `isinstance()` checks
- Raise `TypeError` for invalid types
- Raise `ValueError` for invalid values (empty strings, None, etc.)
- Always include descriptive error messages
- Check for empty strings: `if not value or not value.strip():`

```python
if not isinstance(new_name, str):
    raise TypeError("new_name must be a str instance.")

if not new_name or not new_name.strip():
    raise ValueError("new_name should not be empty.")
```

### Class Design
- Use type hints for class attributes when initialized
- Prefer getter/setter methods over direct attribute access
- Use `uuid.uuid4()` for generating unique IDs, convert to string
- Initialize collections (lists, dicts) in `__init__`

### String Handling
- Use case-insensitive comparisons: `string.casefold()`
- Strip whitespace from user input: `input().strip()`
- Use f-strings for string formatting with variables
- Use regular strings (not f-strings) when no placeholders needed

### Control Flow
- Use `match/case` for multi-way branching (Python 3.10+)
- Each case statement should be on a separate line (avoid inline case statements)
- Use `next()` with generator expressions for finding items in lists

### CLI/Input Handling
- Always validate user input before processing
- Provide clear error messages for invalid input
- Use try/except blocks for operations that may raise exceptions
- Display formatted output with separators (`"="*20`)
