from fastapi import APIRouter

autor_router = APIRouter(
    prefix='/autores',
    tags=['autores']
)


@autor_router.get('/')
def get_autores():
    return {"autores": "Lista de autores"}