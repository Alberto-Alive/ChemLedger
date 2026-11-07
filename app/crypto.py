import hashlib


def hash_file(path: str) -> str:
    with open(path, "rb") as file:
        data = file.read()

    hash_object  = hashlib.sha256(data)

    return hash_object.hexdigest()
    