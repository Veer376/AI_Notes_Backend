from typing import List
from pydantic import BaseModel, EmailStr
class ImageData(BaseModel):
    image: str
    dict_of_vars: dict

class Note(BaseModel):
    value: str
    title: str

class User(BaseModel):
    email: EmailStr
    notes: List[Note]
    
class UserCred(BaseModel):
    email: EmailStr
    password: str # add the length logic, characters, etc.


