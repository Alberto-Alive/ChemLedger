import hashlib
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey
)
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey


from cryptography.hazmat.primitives import serialization

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



def sign_file(path: str, private_key: Ed25519PrivateKey) -> bytes:
    with open(path, "rb") as file:
        data = file.read()

    signature = private_key.sign(data)

    return signature


def verify_file(
    path: str,
    signature:bytes,
    public_key: Ed25519PublicKey,
) -> bool:

    with open(path, "rb") as file:
        date = file.read()
    try:
        public_key.verify(signature, date)
        return True
    except InvalidSignature:
        return False

    
def save_private_key(
    private_key: Ed25519PrivateKey,
    path: str,
    password: bytes,
) -> None:
    
    pem_data = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.BestAvailableEncryption(password)
    )

    with open(path, "wb") as file:
        file.write(pem_data)


def load_private(path: str, password: bytes):
    with open(path, "rb") as file:
        pem_data  =file.read()
    private_key = serialization.load_pem_private_key(
        data=pem_data,
        password=password
    )

    return private_key