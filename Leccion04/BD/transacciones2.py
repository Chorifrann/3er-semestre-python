import psycopg2 as bd  # Esto es para poder conectarnos a Postgre

conexion = bd.connect(user='postgres',password='8546927',host='127.0.0.1',port='5432',database='test_bd')
try:
    conexion.autocommit = False #Aca se inicia la transaccion
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO PERSONA(nombre, apellido, email) VALUES (%s,%s,%s)'
    valores = ('Jorge', 'Prol', 'Jprol@gmail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Juan','Juarez','jcjura@gmail.com', 1)
    cursor.execute(sentencia, valores)

    conexion.commit()#Hacemos el commit manualmente, se cierra la transaccion
    print('Termina la transaccion')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()

conexion.close()