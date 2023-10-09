def validar(**kwargs): # Definimos una función llamada 'validar' que acepta un número variable de argumentos de palabra clave (**kwargs)
   
    for key,value in kwargs.items(): # Iniciamos un bucle que recorre cada par clave-valor en 'kwargs'
        if key=="edad": # Verificamos si la clave es "edad"
            print(isinstance(value,int)) 
        if key=="peso": #Verificamos si la clave es "peso"
            print(isinstance(value,float))
        if key=="estatura":   # Verificamos si la clave es "estatura"
            print(isinstance(value,float))
  

#validar(edad=15,peso=60.0, estatura=1.60)
#validar(edad='siete',peso='39', estatura='1.39')
validar(edad='34',peso=60, estatura=1.90)  # llamamos a la funcion  con valores para verificar sus tipos de datos 


#print(isinstance(60.0,float))