import os
import manage

def main():
    while True:
        print("""Bienvenido al sistema de biblioteca
1. Agregar libro
2. Modificar libro
3. Listar libros
4. Buscar libro
5. Eliminar libro
6. Salir""")
        choice = input("Seleccione una opción: ")
        
        match choice:
            case '1':
                os.system('cls')
                manage.add_book()
                continue
            case '2':
                os.system('cls')
                manage.modify_book()
                input("Presione Enter para continuar...")
                os.system('cls')
                continue
            case '3':
                os.system('cls')
                manage.show_books()
                input("Presione Enter para continuar...")
                os.system('cls')
                continue
            case '4':
                os.system('cls')
                manage.search_book()
                input("Presione Enter para continuar...")
                os.system('cls')
                continue
            case '5':
                os.system('cls')
                manage.delete_book()
                input("Presione Enter para continuar...")
                os.system('cls')
                continue            
            case '6':
                os.system('cls')
                print("Saliendo del sistema.")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")
                os.system('cls')

if __name__ == "__main__":
    os.system('cls')
    main()