from fastapi import APIRouter, Depends, HTTPException
from utils.auth import verify_jwt_token
from utils.encryption import generate_secure_url
from database import db

router = APIRouter()

@router.post("/signup")
def signup(username: str, email: str, password: str):
    encrypted_url = generate_secure_url(email)
    db.users.insert_one({"username": username, "email": email, "password": hash_password(password), "type": "client"})
    return {"encrypted_url": encrypted_url, "message": "Sign-up successful"}

@router.get("/verify-email")
def verify_email(token: str):
    email = decrypt_secure_url(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    db.users.update_one({"email": email}, {"$set": {"verified": True}})
    return {"message": "Email verified successfully"}

@router.get("/files")
def list_files(user=Depends(verify_jwt_token)):
    if user["type"] != "client":
        raise HTTPException(status_code=403, detail="Unauthorized")
    files = db.files.find()
    return {"files": [file["filename"] for file in files]}

@router.get("/download-file/{file_id}")
def download_file(file_id: str, user=Depends(verify_jwt_token)):
    if user["type"] != "client":
        raise HTTPException(status_code=403, detail="Unauthorized")
    
    file = db.files.find_one({"_id": file_id})
    if not file:
        raise HTTPException(status_code=404, detail="File not found")

    secure_url = generate_secure_url(file_id)
    return {"download-link": secure_url, "message": "success"}
