import hashlib


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