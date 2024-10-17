# utils/security.py

def verify_password(plain_password: str, stored_password: str) -> bool:
    return plain_password == stored_password

import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
