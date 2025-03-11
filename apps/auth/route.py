from typing import Union
from fastapi import APIRouter, HTTPException, Request, Response
from models import db
import schema
import bcrypt
from .utils import *

auth_router = APIRouter(prefix='/auth')

@auth_router.get('/test')
def test():
    return {"message" : "auth route working"}

@auth_router.post('/register')
def register(user: schema.UserCred):
    # Check if user already exists
    existing_user = db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=409, detail="Email already registered")
    try:
        db.users.insert_one({"email": user.email, "password": hash_password(user.password)})
        return {"message": "User registered successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)



@auth_router.post('/login', response_model = schema.User)
def login(user: schema.UserCred, response: Response):
    
    existing_user = db.users.find_one({"email": user.email})
    if not existing_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # now we have to check if the user found has the same password or not.
    if not valid_password(user.password, existing_user['password']):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": user.email})
    # print(token)
    response.set_cookie(
        key="token",
        value=token,
        # httponly=True,  # Prevents JavaScript from accessing the token
        secure=True,   # Change to True in production (HTTPS required)
        samesite="None"
    )
    print(token)
    return schema.User(email = existing_user['email'], notes = existing_user.get("notes", []))


@auth_router.get('/getProfile', response_model = schema.User)
def getuser(request: Request):
    
    token = request.cookies.get('token')
    
    if token is None:
        print('No token found')
        raise HTTPException(status_code=401, detail="Invalid token")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = db.users.find_one({"email": payload.get("sub")})
        return schema.User(email = user.get('email'), notes = user.get("notes", []))
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except :
        raise HTTPException(status_code=401, detail="Invalid token")
