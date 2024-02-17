from pydantic import BaseModel
#Cria os identificadores únicos de forma universal
from uuid import UUID, uuid4
from typing import Optional, List
#Trabalhar com lista
from enum import Enum

class Role(str, Enum):
    role_1 = "admin"
    role_2 = "aluna"
    role_3 = "instrutora"

class User(BaseModel):
    id: Optional[UUID] = uuid4() #Criar randomicamente os ids
    first_name: str
    last_name: str
    email: str
    role: List[Role]