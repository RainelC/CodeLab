import random
import os


def desing(fails,secret_word):
    desing = ['''   
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']

    print(desing[fails], "\n")
    i = 0
    for e in range(0, len(secret_word)):
        if secret_word[e] in letters:
            print(secret_word[e], end= " ")
            i += 1
        else:
            print('_', end=" ")
    print()
    return i

def game():
    fails = 0
    score = 0
    secret_word = random.choice(words)
    userLetter = ''
    while fails < 6:
        
        score = desing(fails,secret_word)
        if score == len(secret_word):
            print("FELICIDADES, ADIVINASTE LA PALABRA")
            print()
            break
        userLetter = input("\nIngrese una letra: ").lower()

        if userLetter == " " or userLetter == "":
            os.system('cls')
            print("Debe ingresar una letra!")
        elif userLetter.isnumeric():
            os.system('cls')
            print("Ingrese solo letras, no numeros")
        elif len(userLetter) > 1:
            os.system('cls')
            print("Ingrese solo una letra!")
        elif userLetter in secret_word:
            os.system('cls')
            if userLetter not in letters:
                letters.append(userLetter)
            else:
                print("Letra ya encontrada")
        else:
            os.system('cls')
            fails += 1


    else:
        print("GAME OVER\nSu stickman fue ahorcado, buena suerte la próxima")
        input()

            

        

words = ['python','programación','computadora','desarrollo','interfaz','algoritmo','variable','función','condición','bucle','instrucción','biblioteca','matriz','objeto','herencia','encapsulamiento','polimorfismo','clase','recursividad','archivo']
letters = []

os.system('cls')
print("Bienvenido al juego de El Ahorcado")
print("\nReglas: Se elijira un palabra secreta y usted debe intentar adivinar esta palabra\nletra por letra, cada que falles una palabra se dibujara una parte del Stickman\nsi se dibuja el Stickman completamente, este sera ahorcado y usted perdera la partida.\nGOOD LUCK ")


print('\nPresiona enter para iniciar')
input()
os.system('cls')
game()