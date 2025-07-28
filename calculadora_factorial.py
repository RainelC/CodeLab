import os

def valid_num():
    while True:
        try:
            num = int(input("\033[1;32m"+"Ingrese un número: "+'\033[0;m')) 

        except ValueError: 
            os.system('cls')
            print("\033[1;35m"+"Número invalido. Ingrese un número entero"+'\033[0;m')
            

        if num < 0:
            os.system('cls')
            print("\033[1;35m"+"Número invalido. Ingrese un número positivo"+'\033[0;m')

        else: 
            return num

def CalFactorial():
    num = valid_num()
    fac = num

    for i in range(num-1,0,-1):
        fac = fac * i

    print(f"!{num} = {fac}")


os.system('cls')
print("\033[1;35m"+"Calculadora de Factorial"+'\033[0;m')
print("\033[1;36m"+"\nPresione enter para continuar"+'\033[0;m')
print('\033[?25l', end="")
input()
print('\033[?25h', end="")
os.system('cls')
CalFactorial()

