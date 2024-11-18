from pydantic import BaseModel, EmailStr

class OpsLogin(BaseModel):
    username: str
    password: str

class ClientSignUp(BaseModel):
    username: str
    email: EmailStr
    password: str

class ClientLogin(BaseModel):
    email: EmailStr
    password: str
