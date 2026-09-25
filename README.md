# Task Manager

A desktop task manager built with **CustomTkinter** and **SQLite**. Users can register, log in securely, and manage their own tasks through a simple graphical interface.

## Features

* User registration with input validation
* Password hashing for secure authentication
* Per-user task isolation
* Add, edit, search, and delete tasks
* Task titles and optional descriptions
* Task completion tracking with checkboxes
* Dashboard with task statistics
* AI-powered task advice
* Local SQLite database
* Responsive maximized main window
* Standalone Windows executable with PyInstaller

## Requirements

* Python 3.14+
* Windows, macOS, or Linux
* `uv` (recommended) or `pip`

## Quick Start

### Clone the repository

```bash
git clone https://github.com/mnasseri666/TODO-App.git
cd TODO-App
```

### Install dependencies

Using `uv`:

```bash
uv sync
```

Or using `pip`:

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Then install the project:

```bash
pip install -e .
```

## Run

Using `uv`:

```bash
uv run app
```

Or:

```bash
uv run python -m todo_app.login
```

If the project has been installed with `pip`, you can also run:

```bash
app
```

## Usage

### 1. Register

Click **"Or Register"** and create an account.

* Username: 6–20 characters
* Password: 8–15 characters with letters and numbers
* Full name: optional

Passwords are stored as hashes rather than plaintext passwords.

### 2. Log in

Enter your username and password on the login screen.

Each user's tasks are isolated from other users.

### 3. Manage tasks

After logging in, you can:

* Click **"+"** to add a task
* Search tasks by title
* Open a task to view or edit its details
* Delete tasks
* Mark tasks as finished using the checkbox
* Open the dashboard to view task statistics

### 4. AI Task Advice

The task details window includes an **"advice with AI"** feature that can provide practical suggestions for completing a task.

The AI feature requires an API key configured through an environment variable.

Create a `.env` file in the project directory:

```env
api=your_api_key_here
```

Do not commit `.env` or any API key to Git.

## Project Structure

```text
src/
└── todo_app/
    ├── __init__.py
    ├── login.py              # Login window and application entry point
    ├── register.py           # User registration and validation
    ├── mainApp.py            # Main application window
    ├── show_task_frames.py    # Task list, search, and task management
    ├── task_frame.py         # Individual task widget
    ├── add_task.py            # Add-task dialog
    ├── all_about_task.py      # Task details, editing, and AI advice
    ├── dashboard.py           # Dashboard and task statistics
    ├── paths.py               # Local database path resolution
    │
    └── database/
        ├── __init__.py
        ├── userdatabase.py    # User database and authentication
        ├── tasks_database.py  # Task database operations
        └── check_box_db.py    # Task completion status
```

## Database

The application uses SQLite for local data storage.

The database is created automatically when the application runs.

On Windows, the database is stored at:

```text
%APPDATA%\TODO-App\database.db
```

The database contains information for users, tasks, and task completion status.

Database files are excluded from Git through `.gitignore`.

## Build Executable

PyInstaller can be used to build a standalone Windows executable.

Install the development dependencies:

```bash
uv sync --dev
```

Build using the provided PyInstaller specification:

```bash
uv run pyinstaller TODO-App.spec
```

The executable will be created in:

```text
dist/TODO-App.exe
```

For a release build, the application is configured as a GUI application without a console window.

## Configuration

The application does not require a database configuration file. The SQLite database is created automatically in the user's application-data directory.

The optional AI feature requires an API key:

```env
api=your_api_key_here
```

Keep API keys private and never commit them to the repository.

## Known Limitations

* No automated test suite is currently included.
* The AI feature requires an internet connection and a valid API key.
* AI requests are performed synchronously and may temporarily make the GUI unresponsive while waiting for a response.
* The application is designed primarily as a desktop application rather than a multi-device or cloud-synchronized task manager.

## License

MIT License — free to use, modify, and distribute.
