from capa_datos_persona.conexion import Conexion
from capa_datos_persona.Persona import Persona
from logger_base import log

class PersonaDAO:
    """
    DAO significa : Data Access Object
    CRUD significa:
                    Create = Insertar
                    Read = Seleccionar
                    Update = Actualizar
                    Delete = Eliminar
    """
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s,)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    # Definimos los metodos de clase
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registro = cursor.fetchall()
                personas = [] #Creamos una lista
                for registro in registros:
                    persona + Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(personas)
                return personas
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona insertada: {persona}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido,persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'persona actualizada {persona}' )
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores= (persona.id_persona,)
                cursor.execute(cls._ELIMINAR,valores)
                log.debug(f'los objetos eliminados son: {persona}')
                return cursor.rowcount

if __name__ == '__main__':

    #eliminar un regiustro
    persona1 = Persona(id_persona=13)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f'personas eliminadas: {personas_eliminadas}')

    #actualizar
    #persona1 = Persona(1,'Juan Jose', 'Pena','jpena@mail.com')
    #personas_actualizadas = PersonaDAO.actualizar(persona1)


    #Insertar un registro
    #persona1 = Persona (nombre='Pedro', apellido = 'Romero', email= 'promero@mail.com')
    #personas_insertadas = PersonaDAO.insertar(persona1)
    #log.debug(f'Personas insertadas : {personas_insertadas}')
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug()