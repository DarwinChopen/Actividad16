class Libro:
    def __init__(self, codigo, titulo, autor,anio):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.anio=anio

    def mostrar_info(self):
        return f"Carnet: {self.codigo} - Nombre: {self.titulo} - Edad: {self.autor} - Anio: {self.anio}"
class RegistroLibros:
    def __init__(self):
        self.Libros = {}
    def agregar(self):
        codigoLibro = input("Ingresar el codigo del libro: ")
        if codigoLibro in self.Libros:
            print("Ya existe un libro con ese codigo.\n")
            return

        titulo = input("Ingresar el titulo del autor: ")
        autor= input("Ingrese el auntor del libro")
        anio=int(input("Ingrese el anio de publicacion"))

        self.Libros[codigoLibro] = Libro(codigoLibro, titulo, autor,anio)
        print("Libro agregado.\n")
class Usuario:
    def __init__(self, codigo, nombre,carnet,carrera):
        self.codigo = codigo
        self.nombre = nombre
        self.carrera = carrera

    def mostrar_info(self):
        return f"Carnet: {self.codigo} - Nombre: {self.nombre} - Edad: {self.carnet} - Anio: {self.carrera}"
class RegistroEstudiantes:
    def __init__(self):
        self.usuarios = {}

    def agregar(self):
            carnet = input("Ingresar carnet del estudiante: ")
            if carnet in self.usuarios:
                print("Ya existe un estudiante con ese carnet.\n")
                return

            nombre = input("Ingresar nombre del estudiante: ")
            carrera = int(input("Ingresar la carrera del estudiante: "))

            self.usuarios[carnet] = Usuario(carnet, nombre, carrera)
            print("Estudiante agregado.\n")

registroLib = RegistroLibros()
registroUs=RegistroEstudiantes()
while True:
    print("Menu")
    print("1. Agregar Libros")
    print("2. Agregar Usuarios")
    print("3. Gestion de Prestamos")
    print("4. Salir")
    try:
        opcion=int(input("Ingrese una opcion"))
    except ValueError:
        print("Invalido, Ingrese un entero")
    match opcion:
        case 1:
            registroLib.agregar()
        case 2:
            registroUs.agregar()
        case 3:
            pass
        case 4:
            print("Saliendo....")
            break
        case _:
            print("Opcion Invalida")