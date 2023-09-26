from pydantic import BaseModel, Field
from typing import Optional 


class UsuarioScheme(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre:str
    apellido:str
    email:str
    libros_prestados:int