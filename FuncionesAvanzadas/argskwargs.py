def funcion(*args,**kwargs): # se crea una funcion que acepta un numero variablede argumentos posicionales estos argumentos se agrupan en una tupla "*args", puedes acceder dentro de esos argumentos dentro de la funcion utilizando "*args",Cuando usamos **kwargs indicamos que esta funcion recibe una cantidad variable  de argumentos de palabla clave, estos se almacenan en un diccionario llamado '**kwargs' se utiliza facilmente dentro una funcion.
    
    for elemento in args:  # Iniciamos un bucle 'for' para iterar a través de los argumentos posicionales (que se agrupan en una tupla llamada 'args').
        print(elemento)      # Dentro del bucle, imprimimos cada elemento de 'args'.
    
    for key,val in kwargs.items():  # Comenzamos otro bucle 'for' este recorre los argumentos de la palabra clave.
        print(f'{key} : {val}')      # Imprimimos la clave y el valor de cada argumento de palabra clave en un formato legible.

funcion(1,2,3,4, fecha='6-10-2023',hora='7:30 am') # Llamamos a la función 'funcion' con varios argumentos posicionales y de palabra clave.

x=100  # se creo una variable 'x' se le asigana un valor de 100
print(isinstance(x,int)) #se comprueba si 'x' es instancia de la clase de 'int'(entero) luego se imprime.