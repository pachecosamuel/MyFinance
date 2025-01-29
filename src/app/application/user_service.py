from sqlalchemy.orm import Session
from src.app.domain.user import User
from src.app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def create_user(self, name: str, email: str):
        existing_user = self.user_repo.get_user_by_id(email)
        if existing_user:
            raise ValueError("E-mail já cadastrado!")

        new_user = User(user_id=None, name=name, email=email)
        return self.user_repo.create_user(new_user)
