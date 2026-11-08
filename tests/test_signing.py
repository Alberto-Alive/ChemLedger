from app.crypto import generate_key_pair, sign_file, verify_file

private_key, public_key = generate_key_pair()

path = "samples/experiment_001.csv"

signature = sign_file(path, private_key)


print("Signature:", signature.hex())
print("Verified:", verify_file(path, signature, public_key))