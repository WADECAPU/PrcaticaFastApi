from fastapi import APIRouter
from schemes.libro_scheme import LibroScheme

libro_router = APIRouter(
    prefix='/libros',
    tags=['libros']
)


@libro_router.get('/')
def get_libros():
    return {"libros": "Lista de libros"}


@libro_router.post('/')
def crear_libro(libro:LibroScheme):
    pass