import os
from pathlib import Path


def get_database_path() -> str:
    app_data = Path(os.getenv("APPDATA", Path.home()))

    app_dir = app_data / "TODO-App"
    app_dir.mkdir(parents=True, exist_ok=True)

    return str(app_dir / "database.db")
