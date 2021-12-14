import hashlib
import bcrypt

def hashpwd(password: str) -> str:
    return bcrypt.hashpw(str.encode(password), bcrypt.gensalt()).decode()

def checkpwd(password, bcrypt_hash) -> bool:
    return bcrypt.checkpw(str.encode(password), str.encode(bcrypt_hash))

def blake2b(data: str, size=32, key=""):
    """Hash wrapper for blake2b"""
    return hashlib.blake2b(
        str.encode(data),
        key=str.encode(key),
        digest_size=size
    ).digest()
