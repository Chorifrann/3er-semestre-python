archivo = open('prueba.txt', 'r', encoding='utf8')# las letras son : 'r' , 'a', 'w', 'x'
#print(archivo.read())
#print(archivo.read(16))
#print(archivo.read(10)) #Continuamos desde la linea anterior
#print(archivo.readline())
#print(archivo.readline())

#Vamos a iterar el archivo. cada una de las lineas
#for linea in archivo:
    #print(linea) iteramos todos los elementos del archivo
print(archivo.readlines()[3]) #accedemos al archivo como si fuera una lista