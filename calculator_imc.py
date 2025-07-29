weight = float(input("What is your weight in kilograms?: "))
height = float(input("What is your height in meters: "))
imc = round((weight/height)**2,2)
print("Your IMC is: ", imc)