import random

def es_primo(n):
    if num <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if  n % i == 0:
            return False
        return True
    
n=int(input("cuantos elemnetos desea en la lsita?"))
lista=[]

for i in range(n):
    lista.append(random.randint(1,100))
print("la lista es:",lista)


primos=[]
for num in lista:
    if es_primo(num):
       primos.append(num) 

if len(primos) ==0:
    print("No se encontaron numeros primos en la lista.")
else:
    print("Se encontraron", len(primos), "numeros primos en la lista:")
    print(primos)
