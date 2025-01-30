# src/main.py
from src.app.repositories.user_repository import UserRepository
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.app.infrastructure.orm import SessionLocal
from src.app.domain.user import User
from src.app.api.responses import user_responses, user_example

app = FastAPI()

# Dependência de sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        

@app.post("/users/", response_model=User, responses=user_responses, status_code=201)
def create_user(user: User, db: Session = Depends(get_db)):
    return UserRepository(db).create_user(user)



@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = UserRepository(db).get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user



@app.get("/users/", response_model=list[User])
def get_all_users(db: Session = Depends(get_db)):
    return UserRepository(db).get_all_users()



@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_data: dict, db: Session = Depends(get_db)):
    user = UserRepository(db).update_user(user_id, updated_data)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user



@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    if not UserRepository(db).delete_user(user_id):
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Usuário deletado com sucesso"}
