from pydantic import BaseModel, Field
from typing import Optional 


class LibroScheme(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    autor:str
    isbn: int
    genero: str
    num_copia: int