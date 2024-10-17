import os
from typing import Any
import jwt
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    # Remover o tempo de expiração
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> Any:
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
            options={"verify_exp": False}  # Desativar verificação de expiração
        )
        return payload
    except jwt.PyJWTError:
        return None

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Token inválido")
    user_email = payload.get("sub")
    if user_email is None:
        raise HTTPException(status_code=401, detail="Token inválido")
    return {"email": user_email}

