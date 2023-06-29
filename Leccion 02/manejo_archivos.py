#Declaramos una variable
try:
    archivo = open ('prueba.txt','w', encoding='utf8') # w = write
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo:accion, ejecucioñ y produccion\n')
    archivo.write('las letras son : r (leer), a(anexa), w(escribe), x(crea)\n')
    archivo.write('\nt esta es para texto,\nb archivos binarios, \nw+ leer  y escribir r+\n')
    archivo.write('Saludos a todos los alumnos de la tecnicatura\n')
    archivo.write('\nCon esto terminamos.')
except Exception as e:
    print(e)
finally: #Siempre se ejecuta
    archivo.close() # Con esto se debe de cerrar el archivo
#archivo.write('Todo quedo perfecto') error
