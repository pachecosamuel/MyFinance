# src/app/interfaces/api.py
# from ..application.usecases import create_user
from app.application.usecases import create_user

def main():
    # Criando um usuário como teste
    user = create_user(1, "John Doe", "john.doe@example.com")
    
    # Exibindo o usuário criado
    print("Usuário criado com sucesso!")
    print(user)

if __name__ == "__main__":
    main()
