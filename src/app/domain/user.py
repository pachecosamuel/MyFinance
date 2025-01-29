# src/app/domain/user.py
from src.app.domain.BaseModel import BaseModel
from typing import Optional

class User(BaseModel):
    def __init__(
        self, 
        user_id: int, 
        name: str, 
        email: str, 
        hashed_password: str, 
        is_active: bool = True, 
        role: str = "user", 
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None
    ):
        super().__init__(created_at, updated_at)
        self.user_id = user_id
        self.name = name
        self.email = email
        self.hashed_password = hashed_password
        self.is_active = is_active
        self.role = role

    def __repr__(self):
        return f"User(user_id={self.user_id}, name='{self.name}', email='{self.email}', role='{self.role}')"

    def deactivate(self):
        """Desativa o usuário."""
        self.is_active = False
        self.update_timestamp()
