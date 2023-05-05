#determinar si un numero es o no es primo 

n=int(input("ingresa un numero:"))
x=1
y=0

while x <=n:
    if n % x == 0:
        y= y + 1
    x= x + 1

if y ==2:
    print(f'el numero {n} es primo') 

else:
    print(f'el numero {n} no es primo')       