"""
Script para inicializar/reiniciar la base de datos.
Crea todas las tablas definidas en los modelos.
"""
from db.database import engine, Base
from models.user import Usuario
from models.transaction import Transaction

def init_db():
    Base.metadata.create_all(bind=engine)


def drop_all_tables():
    Base.metadata.drop_all(bind=engine)

def reset_db():
    drop_all_tables()
    init_db()

if __name__ == "__main__":
    reset_db()
