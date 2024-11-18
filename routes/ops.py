from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from utils.auth import verify_jwt_token
from database import db
import os

router = APIRouter()

@router.post("/upload")
def upload_file(file: UploadFile = File(...), user=Depends(verify_jwt_token)):
    if user["type"] != "ops":
        raise HTTPException(status_code=403, detail="Unauthorized")

    if not file.filename.endswith((".pptx", ".docx", ".xlsx")):
        raise HTTPException(status_code=400, detail="Invalid file type")

    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    db.files.insert_one({"filename": file.filename, "uploader_id": user["id"]})
    return {"message": "File uploaded successfully"}
