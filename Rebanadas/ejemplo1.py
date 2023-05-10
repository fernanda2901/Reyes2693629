# crea un codigo que muestre en la pantalla numeros aleatorios y imprima la mitad de la lista de los numeros.

import random
tam=random.randint(5,10)
lista=[random.randrange(100) for i in range (tam)]
rebanada=lista[len(lista)//2:len(lista)]  #(len) tamaño de la lista 
print(lista)
print(rebanada)