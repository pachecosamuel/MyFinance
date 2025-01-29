# src/app/domain/role.py

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.domain.BaseModel import BaseModel

class Role(BaseModel):
    __tablename__ = 'roles'

    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    users = relationship("User", back_populates="roles")
