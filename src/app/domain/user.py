# src/app/domain/user.py
from src.app.domain.BaseModel import BaseModel
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    def __init__(
        self, 
        user_id: int, 
        name: str , 
        email: str, 
        hashed_password: str, 
        is_active: bool = True, 
        role: str = "user", 
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
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
        
    class Config:
        from_attributes = True  # Permite conversão entre ORM e Pydantic
        
        json_schema_extra = {
            "example": {
                "user_id": 1,
                "name": "João Silva",
                "email": "joao.silva@email.com",
                "hashed_password": "hashed_example",
                "is_active": True,
                "role": "user",
                "created_at": "2024-01-29T12:00:00",
                "updated_at": "2024-01-29T12:30:00"
            }
        }
