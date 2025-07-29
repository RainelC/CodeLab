def verifyPali(text):
    text = text.replace(' ', '')
    text = text.lower()
    text_invertido = ""

    for i in range(len(text)-1, -1, -1):
        text_invertido = text_invertido + text[i]

    if text == text_invertido:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")



print("Bienvenido al verificador de palíndromos\nIngrese un texto:")
text = input()

verifyPali(text)