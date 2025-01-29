# src/app/domain/BaseModel.py
from datetime import datetime

class BaseModel:
    def __init__(self, created_at: datetime = None, updated_at: datetime = None):
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def update_timestamp(self):
        self.updated_at = datetime.utcnow()
