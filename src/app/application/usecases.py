# src/app/application/use_cases.py
# from ..domain.models import User
from app.domain.models import User

def create_user(user_id: int, name: str, email: str) -> User:
    """
    Caso de uso para criar um novo usuário.
    """
    return User(user_id, name, email)
