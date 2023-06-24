while True:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    if num1 < num2:
        break
    print("El segundo número debe ser mayor que el primero. Por favor, intente de nuevo.")

diff = num1 - num2
if diff >= num2:
    diff -= num2
    print("El resultado de la resta es:", diff)
else:
    print("El resultado de la resta es:", diff)