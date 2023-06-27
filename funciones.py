from modelos import *
import queries as sql


def agregar_libro():
    nombre = str(input("Ingrese nombre del libro: "))
    paginas = int(input("Ingrese numero de paginas: "))
    genero = int(input("Ingrese el genero del libro: "))
    autor = str(input("Ingrese el autor del libro: "))

    libro = Libros(nombre, paginas, genero, autor)
    sql.agregar_libro(libro)


catalogo = Catalogo("Libros Cristianos")


def listar_libros():
    libros = sql.listar_libros()
    for libro in libros:
        guardar_libro = Libros(libro[1], libro[2], libro[3], libro[4])
        catalogo.Libros.append(guardar_libro)

    for libro in catalogo.Libros:
        print(f"""\
        ====================================================
        Nombre de libro: {libro.nombre}
        Paginas del libro: {libro.paginas} pag
        Genero del libro: {libro.genero}
        Autor del libro: {libro.autor}
        ====================================================
        """)

