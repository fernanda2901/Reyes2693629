def base(funcion): # se crea una función llamada 'base' que acepta otra función 'funcion' como argumento
    
    def interna(n1,n2):  # se crea una función interna llamada 'interna' que toma dos argumentos, 'n1' y 'n2'
        #print('Inicia la función base')
        #print(funcion(n1,n2))#*        
        return funcion(n1,n2)  # Llamamos a la función que se pasó como argumento ('funcion') con 'n1' y 'n2'
        #funcion(n1,n2)
        #print('Finaliza la función base')
    return interna # Retornamos la función interna ('interna') como resultado

def suma(num1,num2): # Definimos una función llamada 'suma' que toma dos argumentos y retorna la suma de ellos
    return num1+num2

def resta(num1,num2): #Definimos otra función llamada 'resta' que toma dos argumentos y retornas la resta de ellos
    return num1-num2

var1=base(suma)  # Creamos una variable 'var1' que almacena el resultado de llamar a 'base' con 'suma' como argumento
var2=base(resta) # Creamos otra variable 'var2' que almacena el resultado de llamar a 'base' con 'resta' como argumento
var1(10,15) # Llamamos a 'var1(10, 15)', que es la función interna generada por 'base' con 'suma' como argumento
var2(15,10) # Llamamos a 'var2(15, 10)', que es la función interna generada por 'base' con 'resta' como argumento

print(var1(10,15)) #Imprimimos el resultado de llamar a 'var1(10, 15)' y 'var2(15, 10)'
print(var2(15,10))