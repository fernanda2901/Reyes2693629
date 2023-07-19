

def ecuacion():
   
    try:
   
        a = float(input("Ingrese el valor de a: "))
        if a == 0:
            raise ZeroDivisionError("El numero ingresado no puede ser 0.")
        
        b = float(input("Ingrese el valor de b: "))
        c = float(input("Ingrese el valor de c: "))

        x1 = (-b + ((b*2) - (4*a*c))*(1/2))/(2*a)
        x2 = (-b - ((b*2) - (4*a*c))*(1/2))/(2*a)
      
 
        print(f"El valor de x1 es: {x1}")
        print(f"El valor de x2 es: {x2}")
      
    except ValueError:
        print("Error, caracter incorrecto.")
        print("Ingrese numeros.")


ecuacion()