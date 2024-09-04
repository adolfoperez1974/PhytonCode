# Solicitar al usuario que ingrese los nombres separados por comas
entrada1 = input("Introduce los nombres separados por comas: ")

# Separar los nombres utilizando split() y eliminar espacios adicionales
entrada2=entrada1.split(",")

entrada3= [nombre.strip() for nombre in entrada2]

# Imprimir cada nombre en una línea diferente
print(f"entrada1= {entrada1}")
print (f"entrada2= {entrada2}")
print(f"entrada3= {entrada3}")
print("entrada4:")
for entrada4 in entrada3:
    print (entrada4)