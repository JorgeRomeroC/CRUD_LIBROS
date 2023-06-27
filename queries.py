import sqlite3
from config import *


def conectar_db():
    conexion = sqlite3.connect(DATABASE_NAME)
    cursor = conexion.cursor()
    return conexion, cursor


# creamos la base de datos
# conectar_db()

def agregar_libro(libro):
    conexion, cursor = conectar_db()
    libro = (
        libro.nombre,
        libro.paginas,
        libro.genero,
        libro.autor
    )
    sql = f"INSERT INTO libro(nombre, paginas, genero, autor) VALUES {libro}"
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def listar_libros():
    conexion, cursor = conectar_db()
    sql = "SELECT * FROM libro"
    cursor.execute(sql)
    libros = cursor.fetchall()
    conexion.close()
    return libros