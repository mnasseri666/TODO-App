# Task Manager

A desktop task manager built with **CustomTkinter** and **SQLite**. Users can register, log in, and manage their own tasks with a modern GUI.

---

## Features

- User registration with validation (username 6–20 chars, password 8–15 chars with letters & numbers)
- Secure login with per-user task isolation
- Add, edit, search, and delete tasks
- Task details with title and description
- Responsive full-screen main window
- Auto-saves to local SQLite database
- Build standalone executable with PyInstaller

---

## Requirements

- Python 3.14+
- Windows / macOS / Linux

---

## Quick Start

```bash
# Clone and enter project
cd SubmitProject

# Create virtual environment
python -m venv .venv

# Activate
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

# Install dependencies
pip install -e ".[dev]"
```

---

## Run

```bash
python -m todo_app.login
```

Or use the installed entry point:

```bash
app
```

---

## Usage

1. **Register** — Click "Or Register", fill in username, password (twice), optional full name
2. **Log in** — Enter credentials on the main screen
3. **Manage tasks**:
   - **+** button → add new task
   - Search bar → filter tasks by title
   - Click a task → open editor to modify or delete
   - "Open dashboard" → experimental dashboard view

---

## Project Structure

```
src/todo_app/
├── login.py              # Login window & entry point
├── register.py           # Registration window with validation
├── mainApp.py            # Main application window
├── show_task_frames.py   # Task list, search, add-task trigger
├── task_frame.py         # Individual task widget (view/edit/delete)
├── add_task.py           # Add/edit task dialog
├── dashboard.py          # dashboard view
├── paths.py              # Database path resolution (APPDATA on Windows)
└── database/
    ├── userdatabase.py   # User CRUD (SQLite)
    └── tasks_database.py # Task CRUD per user (SQLite)
```

---

## Build Executable

```bash
pip install pyinstaller
pyinstaller TODO-App.spec
```

Output: `dist/TODO-App.exe` (Windows)

---

## Configuration

Database location:
- Windows: `%APPDATA%\TODO-App\database.db`
- macOS/Linux: `~/TODO-App/database.db`

---

## Known Limitations

- Passwords stored in plaintext (not hashed) — **not for production use**
- No automated tests yet

---

## License

MIT — free to use, modify, and distribute.