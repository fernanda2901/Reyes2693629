import random #genera números aleatorios.

def llenarLista(tam,rango): #genera una lista de números aleatorios, tam indica el tamaño de la lista, rango indica el rango máximo de los números aleatorios.
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista # devolver la lista resultante desde la función.

def sumaLista(lista):  # se crea la funcion y calcula la suma de los elementos de la lista
    sum=0 
    for x in lista: #for para repetir cada elemento de x de la lista
        sum+=x  #se agrega x a la variable sum.
    return sum #devuelve la funcion de sum para dar el resultado

def compararSuma (lista1,lista2):
    suma1=sumaLista(lista1) #para calcular la suma de los elementos de lista1 y lista2
    suma2=sumaLista(lista2)
    if suma1>suma2:
        mayor=suma1 #se asigna el valor de suma1
        return mayor
    elif suma2>suma1:
        mayor=suma2
        return mayor
    else:
        return f"La suma de los numeros son iguales"
    
def ordenAscen(lista): #se crea una funcion llamada ordenAscen
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]: #se compara el elemento en la posición i con el elemento en la posición j
                aux=lista[i] #para almacenar temporalmente el valor en la posición i
                lista[i]=lista[j]
                lista[j]=aux 
    return lista

def promedioConjunto(lista1,lista2):
    suma=0 #se utilizará para almacenar la suma de todos los números
    for x in lista1: # for para repetir sobre cada elemento de x de la lista1
        suma+=x #se agrega la x a la variable suma(+=)
    for x in lista2:
        suma+=x
    promedio= suma/(len(lista1)+(len(lista2))) #es para dividir la suma de los numeros de las dos listas
    return promedio
# Len para obtener la longitud o cantidad

def promedio(lista):
    suma=0  #con un valor de 0 se utilizarán para contar la cantidad de números 
    for x in lista:
        suma+=x
    promedio= suma/(len(lista1))
    return promedio

def promedioLista(lista1,lista2):
    promedioCon= promedioConjunto(lista1,lista2)
    promedio1= promedio(lista1)
    if promedio1>promedioCon:
        return f"El promedio esta por encima del promedio Conjunto"
    elif promedio1<promedioCon:
        return f"El promedio esta por debajo del promedio Conjunto"
    else:
        return f"El promedio es igual"
    
def pares (lista1,lista2):
    par1=0  #con un valor de 0 se utilizarán para contar la cantidad de números 
    par2=0
    for i in lista1:
        if i%2==0: #se verifica si i es par utilizando la condición i % 2 == 0
            par1+=1 #Si i es par, se incrementa en 1 la variable par1
    for i in lista2:
        if i%2==0: # Si i es divisible por 2 y el resto es igual a 0, i es par
            par2+=1
    if par1>par2:
        return f"{par1} Hay mas numeros par en la lista 1"
    elif par2>par1:
        return f"{par2} Hay mas numeros par en la lista 2"
    else:
        return "Hay igual cantidad de pares en las dos listas"
def impares(lista1,lista2):
    impar1=0 #con un valor de 0 se utilizarán para contar la cantidad de números 
    impar2=0
    for i in lista1:
        if i%2!=0: #si i es impar utilizando la condición i%2!=0 
            #si es diferente entre 2 no es igual a 0, significa que i es impar.
            impar1+=1 #si i es impar se agrga a esta variable
            
    for i in lista2:
        if i%2!=0:
            impar2+=1

    if impar1>impar2:
        return f"{impar1} Hay mas numeros impar en la lista 1"
    elif impar2>impar1:
        return f"{impar2} Hay mas numeros impar en la lista 2"
    else:
        return "Hay igual cantidad de impares en las dos listas"

def numMayor(lista1,lista2):
    mayor1=lista1.pop(-1) #pop en el indice -1 para extraer y eliminar el último elemento de la lista
    mayor2=lista2.pop(-1)
    if mayor1>mayor2:
        return(mayor1) #se devuelve el valor de mayor1 utilizando la instrucción return
    elif mayor2>mayor1:
        return(mayor2)
    else: 
        return f"Los numero mayores son iguales"
    
def numMen(lista1,lista2):
    menor1=lista1.pop(0) #con el índice 0 para extraer y eliminar el primer elemento de la lista
    menor2=lista2.pop(0)
    if menor1<menor2:
        return(menor1)
    elif menor2<menor1:
        return(menor2)
    else: 
        return f"Los numero menores son iguales"


lista1=llenarLista(15,25)
lista2=llenarLista(15,25)
ordenAscen(lista1)
ordenAscen(lista2)
print("1-Suma de cada lista")
print("2-Comparar las dos sumas")
print("3-Promedio Conjunto")
print("4-Promedio de cada lista")
print("5-Comparar el promedio de las dos listas")
print("6-Impar de los listas")
print("7-Par de los listas")
print("8-Numero mayor de las dos listas")
print("9-Numero menor de las dos listas")

selector=1 #se usa para comenzar el bucle y mostrar el menú al principio
while selector!=0: #while se ejecuta mientras el valor de selector sea diferente de 0
    selector=input("Digite la opcion: ")
    match selector: #se utiliza para seleccionar una acción en función del valor de selector
        case "1": # suma de la lista 1 y la suma de la lista 2
            print("Lista 1",lista1)
            print("Lista 2",lista2)
            print("Suma de la lista 1",sumaLista(lista1))
            print("Suma de la lista 2",sumaLista(lista2))
        case "2": #cual es la suma mayor de las dos listas
            print("Lista 1",lista1)
            print("Lista 2",lista2)
            print("La suma mayor de la lista es: ",compararSuma(lista1,lista2))
        case "3": #el promedio  conjunto de la lista1 y lista2
            print("Promedio de las dos lista",promedioConjunto(lista1,lista2))
        case "4": #el promedio de la lista1 y lista2
            print("Promedio de la lista 1",promedio(lista1))
            print("Promedio de la lista 2",promedio(lista2))
        case "5":
            print(promedioLista(lista1,lista2))
            print(promedioLista(lista2,lista1))
        case "6":
            print(impares(lista1,lista2))
        case "7":
            print(pares(lista1,lista2))
        case "8":
            print("Lista 1",lista1)
            print("Lista 2",lista2)
            print(numMayor(lista1,lista2))
        case "9":
            print("Lista 1",lista1)
            print("Lista 2",lista2)
            print(numMen(lista1,lista2))
        case "0":
            break #se ejecuta la instrucción break para salir del bucle y finalizar el programa
