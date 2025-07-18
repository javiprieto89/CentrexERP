import jwt
import datetime
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.models.usuarios import Usuario

SECRET_KEY = "supersecret"  # Cambia por un valor seguro en prod
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, stored_password: str) -> bool:
    """Verify password equality (plaintext for now)."""
    return plain_password == stored_password

def get_password_hash(password: str) -> str:
    """Return the password as-is because we store plaintext for now."""
    return password

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def authenticate_user(db: Session, username: str, password: str):
    """Authenticate a user with plaintext password."""
    user = db.query(Usuario).filter(Usuario.usuario == username).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user

