from fastapi import  APIRouter
from pydantic import BaseModel
from app.core.security import create_token

router = APIRouter()

class AuthInput(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(auth: AuthInput):
    # In a real application, you would verify the username and password
    if auth.username == "admin" and auth.password == "password":
        token = create_token(data={"sub": auth.username})
        return {"access_token": token}
    else:
        return {"error": "Invalid credentials"}
    