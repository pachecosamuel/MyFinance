# src/app/infrastructure/mappers/user_mapper.py
from src.app.domain.user import User
from src.app.infrastructure.orm import UserTable

def user_to_table(user: User) -> UserTable:
    """Converte um objeto de domínio User para a entidade ORM UserTable."""
    return UserTable(
        id=user.user_id,
        name=user.name,
        email=user.email,
        hashed_password=user.hashed_password,
        is_active=user.is_active,
        role=user.role,
        created_at=user.created_at,
        updated_at=user.updated_at
    )

def table_to_user(user_table: UserTable) -> User:
    """Converte uma entidade ORM UserTable para um objeto de domínio User."""
    return User(
        user_id=user_table.id,
        name=user_table.name,
        email=user_table.email,
        hashed_password=user_table.hashed_password,
        is_active=user_table.is_active,
        role=user_table.role,
        created_at=user_table.created_at,
        updated_at=user_table.updated_at
    )
