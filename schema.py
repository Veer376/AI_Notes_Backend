
from pydantic import BaseModel, EmailStr
class ImageData(BaseModel):
    image: str
    dict_of_vars: dict

class User(BaseModel):
    email: EmailStr

class UserCred(User):
    password: str # add the length logic, characters, etc.

class Token(BaseModel):
    token: str
