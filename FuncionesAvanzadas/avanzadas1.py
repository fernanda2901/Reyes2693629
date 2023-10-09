def suma(n1,n2):  # se crea una función llamada 'suma' que toma dos argumentos 'n1' y 'n2' y retorna su suma
    return n1+n2

def resta(n1,n2):  # se crea una una función llamada 'resta' que toma dos argumentos 'n1' y 'n2' y devuelve su resta
    return n1-n2

def producto(n1,n2):  # se crea una una función llamada 'producto' que toma dos argumentos 'n1' y 'n2' y devuelve su producto
    return n1*n2

def division(n1,n2):  # se crea una una función llamada 'division' que toma dos argumentos 'n1' y 'n2' y devuelve su división
    return n1/n2

def operacion(funcion,numero1,numero2):  # se define una funcion 'operacion' que toma aargumentos 
    print(funcion(numero1,numero2))      # -'funcion': una función que realizará una operación matemática
                                         # -'numero1': el primer número para la operación
                                         # -'numero2': el segundo número para la operación
                                         # Esta función ejecuta la función 'funcion' con 'numero1' y 'numero2' como argumentos e imprime el resultado.


operacion(suma,10,5)     #Llamamos a la función 'operacion' con la función 'suma' y los números 10 y 5 como argumentos.
                         #- Esto ejecutará la función 'suma(10, 5)' y mostrará el resultado, que es 15                 