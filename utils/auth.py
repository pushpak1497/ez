from fastapi import HTTPException
import jwt
from passlib.context import CryptContext

SECRET_KEY = "pushpak"
ALGORITHM = "HS256"


pwd_context = CryptContext(
    schemes=["bcrypt"], 
    deprecated="auto"   
)

def hash_password(password: str) -> str:
    
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    
    return pwd_context.verify(password, hashed_password)

def create_jwt_token(data: dict) -> str:
    
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verify_jwt_token(token: str) -> dict:
    
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
