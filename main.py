import funciones

while True:
    menu = int(input("""
[1]Para agregar un libro
[2]Para listar los libros
[0]Para salir del programa
>>> """))
    if menu == 1:
        funciones.agregar_libro()
    elif menu == 2:
        funciones.listar_libros()
    elif menu == 0:
        print("Saliendo del programa...")
        exit()
        