class Libros:
    def __init__(self, nombre, paginas, genero, autor):
        self.nombre = nombre
        self.paginas = paginas
        self.genero = genero
        self.autor = autor
        
class Genero:
    def __init__(self, nombre):
        self.nombre = nombre
        
class Catalogo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.Libros = []
        
        
        