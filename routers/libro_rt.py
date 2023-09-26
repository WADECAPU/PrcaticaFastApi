from fastapi import APIRouter

libro_router = APIRouter(
    prefix='/libros',
    tags=['libros']
)


@libro_router.get('/')
def get_libros():
    return {"libros": "Lista de libros"}