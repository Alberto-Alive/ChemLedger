import hashlib
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey
)
from cryptography.exceptions import InvalidSignature


def generate_key_pair():
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()

    return private_key, public_key


def hash_file(path: str) -> str:
    with open(path, "rb") as file:
        data = file.read()

    hash_object  = hashlib.sha256(data)

    return hash_object.hexdigest()


# sha turns data ( a sequence of bits) into a fixed-size hash
# that acts liek a fingerprint.
# Changing even one bit will almost certainly produce a different hash
# The reason we use the word almost is because there sha does not guarantee uniqueness
# such that different inputs can theoretically produce the same hash (technical term collision)



def sign_file(path: str, private_key: EdEd25519PrivateKey) -> bytes:
    with open(path: str, "rb") as file:
        data = file.read()

    signature = private_key.sign(data)

    return signature