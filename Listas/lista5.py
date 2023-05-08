import random

n= int(input("cuantos elementos desea en la lista?"))
lista=[]

#llenar la lista co numeros aleatorios 
for i in range(n):
    lista.append(random.randint(1,100))

print("la lista generada es:", lista)

#calcular la suma de los numeros pares y el promedio de los numeros impares
suma_pares=0
numeros_impares=[]
suma_impares=0
for numero in lista:
    if numero % 2 ==0:
        suma_pares +=numero
    else:
        numeros_impares.append(numero)
        suma_impares +=numero

if len(numeros_impares) == 0:
    promedio_impares =0
else:
    promedio_impares = suma_impares / len(numeros_impares)

print("La suma de los numeros pares es:", suma_pares)
print("El promedio de los numeros impares es:", promedio_impares)