user_responses = {
    201: {
        "description": "Usuário criado com sucesso",
        "content": {
            "application/json": {
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
        }
    },
    400: {
        "description": "Erro de validação nos dados enviados",
        "content": {
            "application/json": {
                "example": {"detail": "O campo 'email' deve ser um e-mail válido."}
            }
        }
    },
    500: {
        "description": "Erro interno do servidor",
        "content": {
            "application/json": {
                "example": {"detail": "Erro inesperado ao criar o usuário."}
            }
        }
    }
}

user_example = {
    "default": {
                "summary": "Exemplo padrão",
                "description": "Um usuário de exemplo para criação",
                "value": {
                    "user_id": 1,
                    "name": "João Silva",
                    "email": "joao.silva@email.com",
                    "hashed_password": "hashed_example",
                    "is_active": True,
                    "role": "user",
                    "created_at": "2024-01-29T12:00:00",
                    "updated_at": "2024-01-29T12:30:00"
                }
            },
    "admin": {
                "summary": "Usuário administrador",
                "description": "Exemplo de um usuário com permissão de administrador",
                "value": {
                    "user_id": 2,
                    "name": "Maria Admin",
                    "email": "maria.admin@email.com",
                    "hashed_password": "admin_hashed",
                    "is_active": True,
                    "role": "admin",
                    "created_at": "2024-01-29T13:00:00",
                    "updated_at": "2024-01-29T13:30:00"
                }
            }
}