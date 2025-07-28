# Espacio para desarrollar la actividad, si tienes alguna duda o comentario adicional
# lo puedes dejar planteado acá.
import os

##funciones para encriptar y desencriptar

def encode(string,codel):
    count = -1
    dst = code(codel)
    tam = len(codel)-1
    print("\nMensaje encriptado: ",end='')
    for i in string:
        if i in src_str:
            inx = src_str.index(i)
            count += 1
            num = codel.index(codel[count])
            cif = dst[count]
            print(cif[inx], end='')
            if count == tam:
                count = -1
        else:
            print(i,end='')
    print()
                      


def code(key):
    dst_str = []
    for num in key:
        num = int(num)
        d_str = [src_str[num:] + src_str[:num]]
        dst_str = dst_str + d_str
    return dst_str

        

def decode(string, key):
    tam = len(key)-1
    count = -1

    print("\nMensaje desencriptado: ", end='')
    for char in string:
        if char in src_str:
            inx = src_str.index(char)
            count += 1
            i = inx - int(key[count])
            print(src_str[i], end='')
            if count == tam:
                count = -1           
        else:
            print(char, end='')
    print()


##Funciones para los menús

def menu_enconde():
    print("""Vamos a encriptar un mensaje
Primero debe ingresar la frase o palabra que desea encriptar.
Nota: Los números no serán encriptados. La clave debe ser numerica y entera.
Por ultimo la clave, esta clave sera necesaria para desencriptar el mensaje luego.
""")    
    string = input("Ingrese el mensaje a encriptar: ").upper()
    key = input("Ingrese una clave: ")
    key = vali_key(key)
    encode(string,key)
    input("\nPrecione enter para volver al menu principal")
    os.system('cls')

def menu_deconde():
    print("""Vamos a desencriptar un mensaje
Primero debe ingresar la frase o palabra que desea desencriptar.
Por ultimo la clave de desencriptación.
""") 
    string = input("Ingrese el mensaje encriptado: ").upper()
    key = input("Ingrese una clave: ")
    key = vali_key(key)
    decode(string, key)
    input("\nPrecione enter para volver al menu principal")
    os.system('cls')



##funciones para las validaciones
    
def vali_key(key):
    while True: 
        vKey = key
        try:
            vKey = int(vKey)
            return key
        except:
            print("La clave debe ser numerica y entera, ingrese una clave válida")
            key = input("Ingrese una clave: ")



os.system('cls')
src_str = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

while True:
    print("""Encriptar y desencriptar texto
    
1. Encriptar
2. Desencriptar
3. Salir
    
Seleccione una opción: """, end='')
    user_select = input()
    match user_select:
        case "1":
            os.system('cls')
            menu_enconde()
        case "2":
            os.system('cls')
            menu_deconde()
        case "3":
            os.system('cls')
            print("Saliendo-....")
            break
        case _: 
            os.system('cls')
            print("Selección inválida, por favor seleccione nuevamente.")


src_str = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"