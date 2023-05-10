

num = int(input("Ingrese un número: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

def es_perfecto(num):
    suma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i
    if suma_divisores == num:
        return True
    else:
        return False

if es_perfecto(num):
    print(num, "es un número perfecto")
else:
    print(num, "no es un número perfecto")



    
  