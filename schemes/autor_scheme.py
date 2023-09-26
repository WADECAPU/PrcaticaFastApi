from pydantic import BaseModel, Field
from typing import Optional 
from datetime import date

class AutorScheme(BaseModel):
     id: Optional[int] = Field(default=None, primary_key=True)
     nombre:str
     apellido:str
     fecha_nacimiento: date
     pais:str