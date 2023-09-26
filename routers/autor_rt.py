from fastapi import APIRouter
from schemes.autor_scheme import AutorScheme
from config.database import Session
from models import Autor
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

autor_router = APIRouter(
    prefix='/autores',
    tags=['autores']
)


@autor_router.post('/')
def crear_autor(autor:AutorScheme):
    db = Session()
    autor = Autor(**autor.dict())
    db.add(autor)
    db.commit()

    return JSONResponse(status_code=201, content={"mensaje":"Se creó el autor"})


@autor_router.get('/')
def obtener_autores():
    db = Session()
    result = db.query(Autor).all()

    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@autor_router.delete('/{id}')
def eliminar_autor(id:int):
    db = Session()
    db.query(Autor).filter(Autor.id==id).delete()
    db.commit()

    return JSONResponse(status_code=200, content={'mensaje': 'Se elimino el autor'})
