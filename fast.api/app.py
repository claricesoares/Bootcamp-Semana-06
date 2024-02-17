from fastapi import FastAPI, HTTPException
#Ajuda a trabalhar com funcções que recebem 1 argumento que pode ser de mais de um tipo
# from typing import Union
# from pydantic import BaseModel

from typing import List
from models import User, Role
from uuid import UUID, uuid4

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("487ba90f-f08c-4cf0-8862-3dd53e047a24"),
        first_name="Ana",
        last_name="Maria",
        email="email@gmail.com",
        role=[Role.role_1]
    ),
    User(
        id=UUID("03afad79-e6cc-40af-bdda-9fa8ebe7327e"),
        first_name="Clarice",
        last_name="Soares",
        email="email@gmail.com",
        role=[Role.role_2]
    ),
    User(
        id=UUID("c506b0c0-eb01-4093-a9f1-fd688c98d6a9"),
        first_name="Cynthia",
        last_name="Zanoni",
        email="email@gmail.com",
        role=[Role.role_3]
    )
]

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

@app.get("/")
async def root():
    return {"message": "Olá, WoMakers!"}

@app.get("/api/users")
async def get_users():
    return db;

@app.get("/api/users/{id}")
async def get_user(id:UUID):
    for user in db:
        if user.id == id:
            return user
    return{"message": "Usuário não encontrado!"}

@app.post("/api/users")
async def add_user(user: User):
    """
    Adiciona um usuário na base de dados:
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    """
    db.append(user)
    return{"id": user.id}

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o id {id} não encontrado!"
    )

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, busca: Union[str, int] = None):
#     return{"item_id": item_id, "busca": busca}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return{"item_name": item.name, "item_id": item_id}