#cree un codigo que muestre en la pantalla numeros aleatorios hasta el 100, en el rango de 10 a 20 y muestre la cantidad de numeros.

import random #esta funcion es un metodo que devuelve un elemento seleccionado de un numero entero del rango en especifico 
lista=[]
tam=int(random.randint(10,20))
print(tam)
for i in range(tam):
    num=int(random.randrange(100)) #con esta funcion se devuelve un elemento seleccionado aleatoriamente del rango especificado
    lista.append(num)#con esta funcion se agrega un elemento al final de la lista

print(lista)



