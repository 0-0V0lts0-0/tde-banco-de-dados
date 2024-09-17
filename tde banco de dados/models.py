from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Autor(Base):
    __tablename__ = 'autor'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

    livros = relationship('Livro', back_populates='autor')

class Categoria(Base):
    __tablename__ = 'categoria'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

    livros = relationship('Livro', back_populates='categoria')

class Livro(Base):
    __tablename__ = 'livro'

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    genero = Column(String)
    autor_id = Column(Integer, ForeignKey('autor.id'))
    categoria_id = Column(Integer, ForeignKey('categoria.id'))

    autor = relationship('Autor', back_populates='livros')
    categoria = relationship('Categoria', back_populates='livros')
    emprestimos = relationship('Emprestimo', back_populates='livro')

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer)

    emprestimos = relationship('Emprestimo', back_populates='usuario')

class Emprestimo(Base):
    __tablename__ = 'emprestimo'

    id = Column(Integer, primary_key=True)
    livro_id = Column(Integer, ForeignKey('livro.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

    livro = relationship('Livro', back_populates='emprestimos')
    usuario = relationship('Usuario', back_populates='emprestimos')

DATABASE_URL = 'sqlite:///library.db'
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


