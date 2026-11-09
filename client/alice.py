from getpass import getpass
from app.crypto import load_private, sign_file

password = getpass("Private key password: ").encode("utf-8")

private_key =load_private("keys/private_key.pem", password)

signature = sign_file(
    "samples/experiment_001.csv",
    private_key
)

with open("samples/experiment_001.sig", "wb") as file:
    file.write(signature)

print("Experiment signed successfully")