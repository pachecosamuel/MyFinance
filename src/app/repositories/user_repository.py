# src/app/infrastructure/repositories/user_repository.py
from sqlalchemy.orm import Session
from src.app.infrastructure.orm import SessionLocal, UserTable
from src.app.mappers.user_mapper import user_to_table, table_to_user
from src.app.domain.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: User) -> User:
        user_table = user_to_table(user)
        self.db.add(user_table)
        self.db.commit()
        self.db.refresh(user_table)
        return table_to_user(user_table)

    def get_user_by_id(self, user_id: int) -> User | None:
        user_table = self.db.query(UserTable).filter(UserTable.id == user_id).first()
        return table_to_user(user_table) if user_table else None

    def get_all_users(self) -> list[User]:
        users_table = self.db.query(UserTable).all()
        return [table_to_user(user) for user in users_table]

    def update_user(self, user_id: int, updated_data: dict) -> User | None:
        user_table = self.db.query(UserTable).filter(UserTable.id == user_id).first()
        if not user_table:
            return None
        
        for key, value in updated_data.items():
            setattr(user_table, key, value)

        self.db.commit()
        self.db.refresh(user_table)
        return table_to_user(user_table)

    def delete_user(self, user_id: int) -> bool:
        user_table = self.db.query(UserTable).filter(UserTable.id == user_id).first()
        if not user_table:
            return False

        self.db.delete(user_table)
        self.db.commit()
        return True
