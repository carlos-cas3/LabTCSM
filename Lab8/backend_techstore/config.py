# config.py
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Config:
    """Configuración base de la aplicación Flask."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-me")

    DATABASE_PATH = os.environ.get(
        "DATABASE_PATH", os.path.join(BASE_DIR, "database.db")
    )
