from app.crypto import generate_key_pair, sign_file, verify_file, save_private_key, load_private, save_public_key, load_public_key

private_key, public_key = generate_key_pair()

path = "samples/experiment_001.csv"

signature = sign_file(path, private_key)


print("Signature:", signature.hex())
print("Verified:", verify_file(path, signature, public_key))


save_private_key(
    private_key,
    "keys/private_key.pem",
    b"learning-password",
)

loaded_key = load_private(
    "keys/private_key.pem",
    b"learning-password"
)

print(type(loaded_key))

signature = sign_file(
    "samples/experiment_001.csv",
    loaded_key
)


is_valid = verify_file(
    "samples/experiment_001.csv",

    signature,
    public_key
)

print("Signature valid: ", is_valid)




save_public_key(public_key, "keys/public_key.pem")

loaded_public_key = load_public_key("keys/public_key.pem")

print("Loaded public key: ",
verify_file(path, signature, loaded_public_key)
)