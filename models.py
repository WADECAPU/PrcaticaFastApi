from config.database import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship


class Autor(Base):
    __tablename__='autor'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    fecha_nacimiento = Column(Date)
    pais = Column(String)

    libro = relationship('Libro', back_populates='autor')

class Libro(Base):
    __tablename__="libro"
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    autor_id = Column(Integer, ForeignKey('autor.id'))
    isbn = Column(Integer, unique=True)
    genero = Column(String)
    num_copia = Column(Integer)

    autor = relationship('Autor', back_populates='libro')
    
# Ver despues que se hace con esta calse    
class Usuario(Base):
    __tablename__='usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    email = Column(String)
    libros_prestados = Column(Integer)

