
import funciones  #no se como agregar las funciones del otro archivo

def menu():
    while True:
        
        biblioteca = "biblioteca.json"
        print("*" *26)
        print("*        Mundo Libro         *")
        print("*" *26)

        print("[1] - Mantenedor de Autores")
        print("[2] - Reportes")
        print("[3] - Salir")
        opcion = int(input("Ingrese opcion "))

        if opcion == 1:
            while True:
                print("Mantencion de autores")
                print("[1] - Agregar autor")
                print("[2] - Editar autor")
                print("[3] - buscar autor")
                print("[4] - Eliminar autor")
                print("[5] - Salir")
                opcionAutor = int(input("ingrese opcion"))
                if opcionAutor == 1:
                    agregarAutor(biblioteca)
                if opcionAutor == 2:
                    editarAutor(biblioteca)
                if opcionAutor == 3:
                    buscarAutor(biblioteca)
                if opcionAutor == 4:
                    eliminarAutor(biblioteca)
                if opcionAutor == 5:
                    print("saliendo")
                    break
                



        elif opcion == 2:
                print("incompleto")
        elif opcion == 3:
            break


menu()

