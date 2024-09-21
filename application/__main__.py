import os

from application.utils import SETTINGS_LOGGER
from application.run import app  # noqa: F401

if __name__ == "__main__":
    import uvicorn

    is_debug = os.getenv("DEBUG") == "True"
