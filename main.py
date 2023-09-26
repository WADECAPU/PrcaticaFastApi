from fastapi import FastAPI
from routers.libro_rt import libro_router
from routers.autor_rt import autor_router
from routers.usuario_rt import usuario_router
from config.database import engine, Base

app = FastAPI()
app.include_router(libro_router)
app.include_router(autor_router)
app.include_router(usuario_router)

Base.metadata.create_all(bind=engine)

@app.get('/')
def home():
    return {'msj': 'El inicio'}