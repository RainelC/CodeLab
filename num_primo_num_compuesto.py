def es_primo(numero):
    if numero < 2:
        return "Compuesto"  # Los números menores que 2 no son primos ni compuestos
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return "Compuesto"
    return "Primo"

# Imprimir el estado (Primo o Compuesto) para los números del 2 al 12
for num in range(2, 13):
    print(f"{num} : {es_primo(num)}")
