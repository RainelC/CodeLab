def NumMaxMin():
    list = []
    print("Ingresa un número y presiona enter para\nintroducir el siguiete, para dejar de introducir ingresa 0")
    num = ""
    while num != 0:
        num = input("Ingrese un número: ")
        num = ValidInt(num)
        if num != 0:
            list.append(num)

    print(f"El número más pequeño es {min(list)} y el mayor {max(list)}")

def ValidInt(num):
    while True:
        try:
            num = int(num)
            return num 
        except:
            print("Eto' no e' un número entero")
            num = input("Porfa, introduce un número entero: ")

    
    
            

print("Te dire cual es el número más grande y el más pequeño")
NumMaxMin()
