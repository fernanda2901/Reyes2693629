import random
def llenarLista(tam,rango): 
    lista=[random.randrange(rango)for i in range(tam)]
    return lista

#hallar la suma de la lista
def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum 

#hallar el promedio de la lista
def promedioLista(lista):
    return sumaLista(lista)/len(lista)

#hallar el numero mayor de la lista
def mayorLista(l1):
    mayor=0
    for x in l1:
      mayor>=l1
    return mayor
#resultado = mayorLista

print(mayorLista)


l1=llenarLista(4,30)
print("La suma de la lista es", sumaLista(l1))
print(l1)
l1=llenarLista(4,30)
print("El promedio de la lista es:", (round(promedioLista(l1),2)))
print("El numero mayor de la lista es", mayorLista(l1))