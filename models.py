from config.database import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Boolean, Date


class Autor(Base):
    __tablename__='autor'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    fecha_nacimiento = Column(Date)
    pais = Column(String)

class Libro(Base):
    __tablename__="libro"
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    autor = Column(Integer)
    isbn = Column(Integer, unique=True)
    genero = Column(String)
    num_copia = Column(Integer)
    
class Usuario(Base):
    __tablename__='usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    email = Column(String)
    libros_prestados = Column(Integer)