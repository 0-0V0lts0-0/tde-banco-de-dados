from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Autor(Base):
    __tablename__ = 'autor'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

    cds = relationship('Cd', back_populates='autor')


class Categoria(Base):
    __tablename__ = 'categoria'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

    cds = relationship('Cd', back_populates='categoria')


class Cd(Base):
    __tablename__ = 'cd'

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    genero = Column(String)
    autor_id = Column(Integer, ForeignKey('autor.id'))
    categoria_id = Column(Integer, ForeignKey('categoria.id'))

    autor = relationship('Autor', back_populates='cds')
    categoria = relationship('Categoria', back_populates='cds')
    emprestimos = relationship('Emprestimo', back_populates='cd')


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer)

    emprestimos = relationship('Emprestimo', back_populates='usuario')


class Emprestimo(Base):
    __tablename__ = 'emprestimo'

    id = Column(Integer, primary_key=True)
    cd_id = Column(Integer, ForeignKey('cd.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

    cd = relationship('Cd', back_populates='emprestimos')
    usuario = relationship('Usuario', back_populates='emprestimos')


DATABASE_URL = 'sqlite:///library.db'
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

print("As tabelas de CDs foram criadas com sucesso.")
