from fastapi import APIRouter
import schema
from models import db

notes_router = APIRouter(prefix='/notes')

@notes_router.post('/save', response_model=schema.User)
def save_note(user: dict):
    print('inside')
    print(user.get('email'))
    db.users.update_one({"email": user.get('email')}, {"$push": {"notes": {"title": user.get('notes').get('title'), "value": user.get('notes').get('value')}}})
    user = db.users.find_one({"email": user.get('email')})
    return user
