# Task Manager

A desktop task manager built with CustomTkinter and SQLite. Users can register, log in, and manage their own tasks.

## Requirements

- Python 3.10 or newer
- Tkinter (included with most Python installs on Windows)

## Setup

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python login.py
```

1. Register an account (username 6–20 characters; password 8–15 characters with letters and numbers).
2. Log in.
3. Use **+** to add a task, search from the top bar, open a task to edit it, or **remove** to delete it.

The database file is created automatically in the project folder.

## Build an executable (optional)

A PyInstaller spec is included as `TaskManager.spec`:

```bash
pip install pyinstaller
pyinstaller TaskManager.spec
```
