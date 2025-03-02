from datetime import datetime, timedelta, timezone
import bcrypt
import jwt

# config.py & .env content.
SECRET_KEY= 'dfhaiefhweirhifskdjfksadfhailriWERFJDHALF'
ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def valid_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password.encode())

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta if expires_delta else timedelta(days=1))
    to_encode.update({"exp": expire})  # Add expiration time
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
