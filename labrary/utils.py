import os
from book import Book

def validate_code():
    while True:
        code = input("Ingrese el código del libro: ")
        if isinstance(code, str) and len(code) > 0:
            break
        else:
            os.system('cls')
            print("Código del libro inválido. Intente de nuevo.")
            continue
    return code

def validate_title():
    while True:
        title = input("Ingrese el título del libro: ")
        if isinstance(title, str) and len(title) > 0:
            break
        else:
            os.system('cls')
            print("Título inválido. Intente de nuevo.")
            continue
    return title

def validate_author():
    while True:
        author_last_name = input("Ingrese el apellido del autor: ")
        author_first_name = input("Ingrese el nombre del autor: ")
        if isinstance(author_last_name, str) and len(author_last_name) > 0 and isinstance(author_first_name, str) and len(author_first_name) > 0:
           break
        else:
            os.system('cls')
            print("Nombre o apellido del autor inválido. Intente de nuevo.")
            continue
    return author_last_name, author_first_name 

def validate_knowledge_area():
    while True:
        knowledge_area = input("Ingrese el área de conocimiento: ")
        if isinstance(knowledge_area, str) and len(knowledge_area) > 0:
            break
        else:
            os.system('cls')
            print("Área de conocimiento inválida. Intente de nuevo.")
            continue
    return knowledge_area

def validate_publisher():
    while True:
        publisher = input("Ingrese el publicador: ")
        if isinstance(publisher, str) and len(publisher) > 0:
            break
        else:
            os.system('cls')
            print("Publicador inválido. Intente de nuevo.")
            continue
    return publisher

def validate_assigned_section():
    while True:
        assigned_section = input("Ingrese el tramo asignado: ")
        if isinstance(assigned_section, str) and len(assigned_section) > 0:
            break
        else:
            os.system('cls')
            print("Tramo asignado inválido. Intente de nuevo.")
            continue
    return assigned_section

def validate_book(): 
    code = validate_code()
    title = validate_title()
    author_last_name, author_first_name = validate_author()
    knowledge_area = validate_knowledge_area()
    publisher = validate_publisher()
    assigned_section = validate_assigned_section()
    return Book(code, title, author_last_name, author_first_name, knowledge_area, publisher, assigned_section)