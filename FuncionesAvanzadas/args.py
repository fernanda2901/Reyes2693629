# def suma(num1,num2):
#     return num1+num2
#     #print(num1+num2)


def suma(*args):     # *args, se utiliza para aceptar un número variable de argumentos en una función, los argumentos se agrupan en una tupla 
    print(type(args)) # se imprime el tipo de dato

def mayor(*args):
    m=0             # Inicializamos una variable "m" en 0 para mantener un seguimiento del valor más grande.
    for i in args:  #Recorremos todos los argumentos pasados a la función
        
        if i>m:    # Comparamos cada argumento con el valor actual de "m"
            m=i    # Si el argumento es mayor que el valor actual de "m", actualizamos "m" con ese valor
    return m       # Devolvemos el valor más grande encontrado en los argumentos

print(mayor(10,23,21,100,1000,1,2,3)) # utilizamos este print para mostrar el resultado de la funcion se proporciona argumentos particulares.

#suma(10,23,21)
#suma('hola',122,[],{})