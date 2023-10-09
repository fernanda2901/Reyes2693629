def function(**kwargs): # Definimos una función llamada 'function' que acepta argumentos de palabra clave (**kwargs)
    #print(type(kwargs))
    for key in kwargs.keys():   # Iteramos a través de lasclave (keys) de 'kwargs' y las imprimimos
        print(key)
    for value in kwargs.values(): # Iteramos a través de los valores (values) de 'kwargs' y los imprimimos
         print(value)
    for key,value in kwargs.items():  # Iteramos a través de los pares clave-valor de 'kwargs' y los imprimimos en formato "clave : valor"
        print(f'{key} : {value}')


function(programa="adso",ficha=2693629,aprendices=16) # Llamamos a la función 'function' y le pasamos argumentos de palabra clave