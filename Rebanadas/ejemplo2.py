#Llenar una lista con numero aleatorios (reales con un decimal) que representen calificaciones de un curso. Se evalúa de 0 a 5.
#El curso puede tener entre 20 y 30 aprendices
#Genere listas nuevas para los aprobados y los reprobados (Se aprueba con 3)



import random
tam=random.randint(20,30)
lista=[random.randrange(0,6) for i in range (tam)]

Reprobados=[]
aprobados=[]



for i in range (len(lista)):
     if(lista[i]<= 2):
         Reprobados.append(lista[i])
else:
    aprobados.append(lista[i])
    
    
print("Lista original:", lista)
print("Reprobados:", Reprobados)
print("aprobados:",aprobados)
x=int(input("Ingrese su nota: "))
if x <=2:
    print("Usted reprobo")
if x >=6:
    print("esa nota sale del rango")
else:
    print("Usted aprobo")