def base(funcion):  #se crea una función llamada "base" que toma una función como argumento
    
    def interna(): #dentro de la funcion 'base' se crea otra funcion  llamada "interna"
        print('Inicia la función base')
        funcion()    # Llamamos a la función que pasó como argumento ('funcion'). 
        print('Finaliza la función base')
    return interna   # Retornamos la función interna ('interna') como resultado

def integrada(): # se crea función llamada 'integrada'
    print('Funcion Integrada')

def otraFuncion(): # se crea otra función llamada 'otraFuncion'
    print('Otra Funcion')

var1=base(integrada)  # Creamos una variable 'var1' que almacena el resultado de llamar a 'base' con 'integrada' como argumento
var2=base(otraFuncion) # Creamos otra variable 'var2' que almacena el resultado de llamar a 'base' con 'otraFuncion' como argumento

var1() # Llamamos a 'var1', que es la función interna generada por 'base' con 'integrada' como argumento
var2()# Llamamos a 'var2', que es la función interna generada por 'base' con 'otraFuncion' como argumento