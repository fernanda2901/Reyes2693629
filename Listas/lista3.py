import random 

n=int(input("ingrese el tamaño de la lista"))
lista=[]

for i in range(n):
    lista.append(random.randint(1,100))

print("la lista original es:", lista)

suma=sum(lista)
print("El promedio de la suma es:", suma)

promedio=suma/n
print("el promedio de la lista es:", promedio)

menor=min(lista) #se utiliza lafuncion min() para encontrar el numero menor en la lista.
asendentes= sorted(lista)
print("el numero menor de la lista es", menor)
print("lista ordenada de manera asendentes", asendentes)

descendentes= sorted(lista, reverse=True )
print("lista ordenada de una forma descendente", descendentes)

frecuencia={}
for elemento in lista:
    if elemento in frecuencia:
        frecuencia[elemento] +=1

    else:
        frecuencia[elemento] =1

moda=max(frecuencia, key=frecuencia.get)
print("lamoda de la lista es",moda)

numero=int(input("ingrese el numero que se desea buscar:"))
if numero in lista:
    posicion=lista.index(numero)
    print("el numero", numero, "se encuentra en la posicion", posicion)
else:
    print("el numero",numero, "no se encuentra en la lista")

num=int(input("que numero desea buscar?"))
pos=-1
for i in range(n):
    pos=i
    break 
if pos !=-1:
    print("el numero",num, "se encuentra en la posicion", pos, " de la lista.")
else:
    print("el numero", num, "no se encuentra en la lista.")
