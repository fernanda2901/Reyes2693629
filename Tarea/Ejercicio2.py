
inicio = int(input("Ingrese el número de inicio: "))
fin = int(input("Ingrese el número de fin: "))
cantidad = int(input("Ingrese la cantidad a incrementar o decrementar: "))

# Imprimir serie
if inicio < fin:
    serie = list(range(inicio, fin + 1, cantidad))
else:
    serie = list(range(inicio, fin - 1, -cantidad))

print("Serie:", serie)

# Contar múltiplos
num = int(input("Ingrese un número positivo: "))
while num < 0:
    num = int(input("El número ingresado no es positivo. Ingrese un número positivo: "))

n = int(input("Ingrese el valor de n para buscar múltiplos: "))

multiplos = [i for i in serie if i <= num and i % n == 0]
cantidad_multiplos = len(multiplos)

print(f"La cantidad de múltiplos de {n} entre 0 y {num} es {cantidad_multiplos}.")