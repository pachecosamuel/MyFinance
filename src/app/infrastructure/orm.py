# src/app/infrastructure/orm.py
from sqlalchemy import Column, Integer, Float, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine("sqlite:///app.db", echo=True)
Base.metadata.create_all(engine)

class UserTable(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

class BudgetTable(Base):
    __tablename__ = "budgets"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    total = Column(Float, nullable=False)
