from app.crypto import load_public_key, verify_file


public_key = load_public_key("keys/public_key.pem")

with open("samples/experiment_001.sig", "rb") as file:
    signature = file.read()

is_valid = verify_file(
    "samples/experiment_001.csv",
    signature,
    public_key,
)

print("Signature valid: ", is_valid)