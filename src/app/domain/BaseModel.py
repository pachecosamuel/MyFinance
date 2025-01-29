from sqlalchemy import Column, Integer, DateTime
from datetime import datetime

class Base:
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
class BaseModel(Base):
    __abstract__ = True  # Isso garante que a tabela não seja criada diretamente
    # Adicione aqui lógica compartilhada (métodos ou atributos)
