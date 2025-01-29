from sqlalchemy.orm import Session
from src.app.infrastructure.orm import UserTable
from src.app.mappers.user_mapper import user_table_to_entity, entity_to_user_table
from src.app.domain.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, user_id: int) -> User:
        user_table = self.db.query(UserTable).filter(UserTable.id == user_id).first()
        return user_table_to_entity(user_table) if user_table else None

    def create_user(self, user: User):
        user_table = entity_to_user_table(user)
        self.db.add(user_table)
        self.db.commit()
        self.db.refresh(user_table)
        return user_table_to_entity(user_table)
