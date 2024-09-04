def multip(lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion = multiplicacion * i
    print(multiplicacion)

# Solicitar al usuario que ingrese números separados por comas
entrada = input("Introduce los números a multiplicar separados por comas: ")

# Convertir la cadena de entrada en una lista de enteros
# Separamos la cadena en base a la coma y convertimos a entero
numeros = [int(num) for num in entrada.split(',')]

# Llamar a la función con la lista de números
multip(numeros)