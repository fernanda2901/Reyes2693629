n = int(input("Ingrese un número entero: "))

# Inicializamos la variable sum en 0
sum = 0

# Recorremos los posibles divisores de n con un ciclo for
for i in range(1, n):
    if n % i == 0:
        sum += i

# Si la suma de los divisores de n es igual a n, entonces n es un número perfecto
if sum == n:
    print(n, "es un número perfecto")
else:
    print(n, "no es un número perfecto")