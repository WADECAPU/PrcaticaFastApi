from fastapi import APIRouter

usuario_router = APIRouter(
    prefix='/usuarios',
    tags=['usuarios']
)


@usuario_router.get('/')
def get_usuario():
    return {"usuarios": "Lista de usuarios"}