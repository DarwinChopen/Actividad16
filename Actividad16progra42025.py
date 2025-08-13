while True:
    print("Menu")
    print("1. Agregar Libros")
    print("2. Agregar Usuarios")
    print("3. Gestion de Prestamos")
    print("4. Salir")
    try:
        opcion=int("Ingrese una opcion")
    except ValueError:
        print("Invalido, Ingrese un entero")
    match opcion:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            print("Saliendo....")
            break
        case _:
            print("Opcion Invalida")