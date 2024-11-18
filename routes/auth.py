from fastapi import APIRouter, HTTPException
from utils.auth import create_jwt_token, hash_password, verify_password 
from database import db

router = APIRouter()

@router.post("/login")
def login(username: str, password: str, user_type: str):
    user = db.users.find_one({"username": username, "type": user_type})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_jwt_token({"id": str(user["_id"]), "type": user_type})
    return {"access_token": token, "message": "Login successful"}
