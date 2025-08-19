import os
from utils import *

books = []

def show_books():
    if not books:
        os.system('cls')
        print("No hay libros registrados.")
    else:
        os.system('cls')
        print("Lista de libros:")
        for book in books:
            print(f"Código: {book.code}, Título: {book.title}, Autor: {book.author_first_name} {book.author_last_name}, Área: {book.knowledge_area}, Publicador: {book.publisher}, Tramo: {book.assigned_section}")

def search_book():
    if not books:
        os.system('cls')
        print("No hay libros registrados.")
        return
    code = input("Ingrese el código del libro a buscar: ")
    for book in books:
        if book.code.lower() == code.lower():
            print(f"Libro encontrado: {book.title} por {book.author_first_name} {book.author_last_name}")
            break
    else:
        os.system('cls')
        print("Libro no encontrado.")

def add_book():
    new_book = validate_book()
    books.append(new_book)
    os.system('cls')
    print("Libro agregado exitosamente.")

def modify_book():
    if not books:
        os.system('cls')
        print("No hay libros registrados.")
        return
    code = input("Ingrese el código del libro a modificar: ")
    for book in books:
        if book.code.lower() == code.lower():
            print("Deje vacío el campo que no desea modificar.")
            nuevo_titulo = input("Nuevo título: ")
            if nuevo_titulo.strip():
                book.title = nuevo_titulo

            nuevo_apellido = input("Nuevo apellido del autor: ")
            if nuevo_apellido.strip():
                book.author_last_name = nuevo_apellido

            nuevo_nombre = input("Nuevo nombre del autor: ")
            if nuevo_nombre.strip():
                book.author_first_name = nuevo_nombre

            nueva_area = input("Nueva área de conocimiento: ")
            if nueva_area.strip():
                book.knowledge_area = nueva_area

            nuevo_publicador = input("Nuevo publicador: ")
            if nuevo_publicador.strip():
                book.publisher = nuevo_publicador

            nuevo_tramo = input("Nuevo tramo asignado: ")
            if nuevo_tramo.strip():
                book.assigned_section = nuevo_tramo

            os.system('cls')
            print("Libro modificado exitosamente.")
            break
    else:
        os.system('cls')
        print("Libro no encontrado.")

def delete_book():
    if not books:
        os.system('cls')
        print("No hay libros registrados.")
        return
    code = input("Ingrese el código del libro a eliminar: ")
    for book in books:
        if book.code.lower() == code.lower():
            books.remove(book)
            print("Libro eliminado exitosamente.")
            break
    else:
        os.system('cls')
        print("Libro no encontrado.")