#determinar los divisores de un numero introducido por teclado

a=int(input('ingrese un numero'))

print(f'los divisores de {a} son:')

for i in range (1,a+1):
    if a % i ==0:
        print(i)
