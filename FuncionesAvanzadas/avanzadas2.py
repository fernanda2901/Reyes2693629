def base(x): # se define la funcion 'base' toma como argumento y 
    
    def suma(y): #se crea una funcion interna suma' que toma un argumento 'y'
        return x+y ## Devolvemos la suma de 'x' e 'y'
        #print(x+y)
    
    def resta(y):  #se crea otra función interna 'resta' que toma un argumento 'y'
        return x-y  # retornamos la resta de 'x' y 'y'
    
    return [suma,resta] #retornamos una lista que contiene las funciones 'suma' y 'resta'
                        # La función 'base' toma un argumento 'x' y devuelve una lista que contiene las funciones 'suma' y 'resta'
#print(base(1))

usoFuncionRetornada=base(10) #Llamamos a la función 'base' con 'x' igual a 10 y guardamos el resultado en 'usoFuncionRetornada'

print(usoFuncionRetornada[1](20))  # Llamamos a la función 'resta' (que está en la posición 1 de la lista devuelta por 'base') con 'y' igual a 20 y luego imprimimos el resultado