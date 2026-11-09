from pathlib import Path
from uuid import uuid4

STORAGE_DIR =Path("data/uploads")

def save_experiments(data: bytes) -> str:
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    name_file = f"{uuid4()}.csv"
    path = STORAGE_DIR / name_file

    with open(path, "wb") as file:
        file.write(data)
    return str(path)