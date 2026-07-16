'''Grupo: 2
Integrantes: Abarca Orrala Pedro Segundo, Delacruz Castillo Henry Alexander, 
Lopez Mendoza Genessis Milena, Piedra Ortega Francisco Andres, 
Quinde Eugenio Julexi Tatiana'''
# Librerías
import os  # Permite trabajar con carpetas y rutas del sistema operativo
import sqlite3  # Importa la librería sqlite3 para trabajar con bases de datos SQLite
from collections import deque  # Importa la estructura deque,que se utilizará como una cola (FIFO)
from tkinter import *  # Importa todos los componentes de Tkinter para crear la interfaz gráfica
from tkinter import messagebox  # Importa cuadros de diálogo para mostrar mensajes al usuario
from tkinter import ttk  # Permite mostrar información en forma de tabla dentro de la interfaz

# ==========================================================
# VARIABLES GLOBALES
# ==========================================================
cola_espera = deque()  # Cola utilizada para administrar la sala de espera

pila_historial = []  # Pila utilizada para almacenar los historiales recientes

lista_citas = ListaDoblementeEnlazada()  # Crea la lista doblemente enlazada que administrará las citas

# ===========================================
# CLASE DEL DOMINIO
# ===========================================

# Se crea la clase Persona para representar la información
# común que tendrán pacientes y médicos.
class Persona:
    # Constructor de la clase Persona.
    # Se ejecuta automáticamente cuando se crea un objeto.
    def __init__(self, nombre, cedula):
        self.__nombre = nombre  # Guarda el nombre como un atributo privado
        self.__cedula = cedula  # Guarda la cédula como un atributo privado.

    def get_nombre(self):
        return self.__nombre  # Devuelve el nombre
    
    def get_cedula(self):
        return self.__cedula  # Devuelve la cédula

    # Permite modificar el nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Permite modificar la cédula
    def set_cedula(self, cedula):
        self.__cedula = cedula

    # Muestra los datos de la persona
    def mostrar_datos(self):
        print("Nombre:", self.__nombre)
        print("Cédula:", self.__cedula)
        
# La clase Paciente hereda los atributos y métodos
# de la clase Persona.
class Paciente(Persona):

    # Constructor de la clase Paciente.
    def __init__(self, id_paciente, nombre, cedula, edad, telefono):
        super().__init__(nombre, cedula)   # Llama al constructor de la clase Persona
        self.__id_paciente = id_paciente  # Guarda el identificador del paciente
        self.__edad = edad  # Guarda la edad
        self.__telefono = telefono  # Guarda el teléfono

    # Devuelve el ID
    def get_id(self):
        return self.__id_paciente

    # Devuelve la edad
    def get_edad(self):
        return self.__edad

    # Devuelve el teléfono
    def get_telefono(self):
        return self.__telefono

    # Permite modificar la edad
    def set_edad(self, edad):
        self.__edad = edad

    # Permite modificar el teléfono
    def set_telefono(self, telefono):
        self.__telefono = telefono
    # Muestra toda la información del paciente
    def mostrar_datos(self):

        print("ID:", self.__id_paciente)

        print("Nombre:", self.get_nombre())

        print("Cédula:", self.get_cedula())

        print("Edad:", self.__edad)

        print("Teléfono:", self.__telefono)

# La clase Medico hereda de Persona.
class Medico(Persona):

    # Constructor.
    def __init__(self, id_medico, nombre, cedula,
                 especialidad, telefono, consultorio):

        # Llama al constructor de Persona.
        super()._init_(nombre, cedula)

        # Guarda el ID.
        self.__id_medico = id_medico

        # Guarda la especialidad.
        self.__especialidad = especialidad

        # Guarda el teléfono.
        self.__telefono = telefono

        # Guarda el consultorio.
        self.__consultorio = consultorio

    # Métodos Get y Devuelve el ID
    def get_id(self):
        return self.__id_medico

    def get_especialidad(self):
        return self.__especialidad

    def get_telefono(self):
        return self.__telefono

    def get_consultorio(self):
        return self.__consultorio

    # Permite modificar la especialidad
    def set_especialidad(self, especialidad):
        self.__especialidad = especialidad

    # Permite modificar el teléfono
    def set_telefono(self, telefono):
        self.__telefono = telefono

    # Permite modificar el consultorio
    def set_consultorio(self, consultorio):
        self.__consultorio = consultorio

    # Muestra la información del médico
    def mostrar_datos(self):

        print("ID:", self.__id_medico)

        print("Nombre:", self.get_nombre())

        print("Cédula:", self.get_cedula())

        print("Especialidad:", self.__especialidad)

        print("Teléfono:", self.__telefono)

        print("Consultorio:", self.__consultorio)

# Representa una cita médica.
class Cita:

    # Constructor.
    def __init__(self, id_cita, fecha, hora, estado,id_paciente,id_medico):

        # Guarda el ID
        self.__id_cita = id_cita # Guarda el ID de la cita como un atributo privado

        # Guarda la fecha
        self.__fecha = fecha # Guarda la fecha de la cita como un atributo privado

        # Guarda la hora
        self.__hora = hora # Guarda la hora de la cita como un atributo privado

        # Guarda el estado
        self.__estado = estado # Guarda el estado de la cita como un atributo privado

        # Guarda el paciente asociado
        self.__id_paciente = id_paciente

        # Guarda el médico asociado
        self.__id_medico = id_medico
    # Métodos Get

    def get_fecha(self):
        return self.__fecha # Devuelve la fecha de la cita

    def get_hora(self):
        return self.__hora # Devuelve la hora de la cita

    def get_estado(self):
        return self.__estado # Devuelve el estado de la cita

    def get_id_paciente(self):
        return self.__id_paciente

    def get_id_medico(self):
        return self.__id_medico
        
    def get_id(self):
    return self.__id_cita
# Representa el historial de un paciente.
class HistorialClinico:

    # Constructor
    def __init__(self, id_historial, fecha,
                 diagnostico, tratamiento,id_paciente): #Constructor de la clase.Se ejecuta automáticamente al crear un objeto.

        # Guarda el ID
        self.__id_historial = id_historial # Guarda el ID del historial clínico como un atributo privado

        # Guarda la fecha
        self.__fecha = fecha # Guarda la fecha del historial clínico como un atributo privado

        # Guarda el diagnóstico
        self.__diagnostico = diagnostico # Guarda el diagnóstico del historial clínico como un atributo privado

        # Guarda el tratamiento
        self.__tratamiento = tratamiento # Guarda el tratamiento del historial clínico como un atributo privado

        # Guarda el paciente asociado.
        self.__id_paciente = id_paciente
                     
    # Devuelve la fecha
    def get_fecha(self):
        return self.__fecha

    # Devuelve el diagnóstico
    def get_diagnostico(self):
        return self.__diagnostico

    # Devuelve el tratamiento
    def get_tratamiento(self):
        return self.__tratamiento

    # Devuelve el ID del paciente
    def get_id_paciente(self):
        return self.__id_paciente

# ===========================================
# ESTRUCTURA DE DATOS
# ===========================================
# Crea una cola vacía
cola_espera = deque()

# Función para ingresar un paciente
def ingresar_cola(nombre):

    # Agrega el paciente al final
    cola_espera.append(nombre)

# Función para atender
def atender_paciente():
    # Verifica si existen pacientes
    if len(cola_espera) > 0:

        # Elimina y devuelve el primer paciente
        return cola_espera.popleft()

    # Si no existen pacientes devuelve None
    return None
# Devuelve todos los pacientes que se encuentran esperando
def mostrar_cola():

    # Convierte la cola en una lista
    return list(cola_espera)

# Inserta una nueva atención en la parte superior de la pila
def agregar_historial(registro):

    # Agrega el nuevo registro
    pila_historial.append(registro)

# Consulta la última atención
def ultima_atencion():

    # Comprueba que existan registros
    if len(pila_historial) > 0:

        # Devuelve el último elemento
        return pila_historial[-1]

    return None

# Elimina el historial más reciente
def eliminar_ultima_atencion():

    # Comprueba que existan elementos
    if len(pila_historial) > 0:

        # Elimina el último historial
        pila_historial.pop()

# Representa un nodo de la lista
class Nodo:
    def __init__(self, dato):  # Constructor
        self.dato = dato  # Guarda el dato
        self.siguiente = None  # Nodo siguiente
        self.anterior = None  # Nodo anterior

# Representa la agenda de citas
class ListaDoblementeEnlazada:
    def __init__(self):  # Constructor
        self.inicio = None  # Inicio de la lista
        self.fin = None  # Último nodo
    # Inserta una cita
    def insertar(self, dato):
        nuevo = Nodo(dato)  # Crea un nuevo nodo
        # Si la lista está vacía
        if self.inicio is None:
            self.inicio = nuevo  # El nuevo nodo será el primero
            # También será el último
            self.fin = nuevo
        else:

            # Conecta el nuevo nodo con el último
            self.fin.siguiente = nuevo

            # Guarda la referencia al nodo anterior
            nuevo.anterior = self.fin

            # Actualiza el último nodo
            self.fin = nuevo

    # Devuelve todas las citas almacenadas
    def recorrer(self):

        # Lista temporal
        datos = []

        # Empieza desde el inicio
        actual = self.inicio

        # Recorre toda la lista
        while actual is not None:

            # Guarda el dato del nodo
            datos.append(actual.dato)

            # Avanza al siguiente nodo
            actual = actual.siguiente

        # Devuelve todas las citas
        return datos   

# ==========================================================
# BASE DE DATOS
# ==========================================================

# CONFIGURACIÓN DE LA BASE DE DATOS

# Obtiene automáticamente la carpeta Documentos del usuario.
ruta_documentos = os.path.join(os.path.expanduser("~"), "Documents")

# Crea la ruta completa donde se almacenará la base de datos.
ruta_base_datos = os.path.join(ruta_documentos, "clinica.db")
def conectar_bd():

    # Crea la conexión con la base de datos.
    conexion = sqlite3.connect(ruta_base_datos)

    # Devuelve la conexión para que pueda ser utilizada
    # por otras funciones del programa.
    return conexion
    
# Esta función crea todas las tablas del sistema.
# Solo se crearán una vez.
# Si las tablas ya existen, SQLite no las volverá a crear.

def crear_tablas():

    # Se establece la conexión con la base de datos.
    conexion = conectar_bd()

    # Se crea un cursor para ejecutar instrucciones SQL.
    cursor = conexion.cursor()
    
    # Crea la tabla de paciente.
    cursor.execute("""

        CREATE TABLE IF NOT EXISTS paciente(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL,

            cedula TEXT UNIQUE NOT NULL,

            edad INTEGER NOT NULL,

            telefono TEXT NOT NULL

        )

    """)

# Crea la tabla de médico.
    cursor.execute("""

        CREATE TABLE IF NOT EXISTS medico(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL,

            cedula TEXT UNIQUE NOT NULL,

            especialidad TEXT NOT NULL,

            telefono TEXT NOT NULL,

            consultorio TEXT NOT NULL

        )

    """)

# Crea la tabla donde se almacenarán todas las cita.
    cursor.execute("""

        CREATE TABLE IF NOT EXISTS cita(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            fecha TEXT NOT NULL,

            hora TEXT NOT NULL,

            estado TEXT NOT NULL,

            id_paciente INTEGER NOT NULL,

            id_medico INTEGER NOT NULL,

            FOREIGN KEY(id_paciente) REFERENCES pacientes(id),

            FOREIGN KEY(id_medico) REFERENCES medicos(id)

        )

    """)
    # Crea la tabla del historial clínico.
    cursor.execute("""

        CREATE TABLE IF NOT EXISTS historial_clinico(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            fecha TEXT NOT NULL,

            diagnostico TEXT NOT NULL,

            tratamiento TEXT NOT NULL,

            id_paciente INTEGER NOT NULL,

            FOREIGN KEY(id_paciente) REFERENCES pacientes(id)

        )

    """)
    # GUARDAR LOS CAMBIOS
    # ------------------------------------------------------

    # Guarda todas las tablas creadas.
    conexion.commit()

    # Cierra la conexión.
    conexion.close()
    # Cuando el programa inicie se crearán automáticamente
# todas las tablas del sistema.
crear_tablas()
# ===========================================
# INTERFAZ GRÁFICA
# ===========================================

# REGISTRAR PACIENTE
# ----------------------------------------------------------

# Esta función recibe un objeto Paciente y lo almacena
# en la base de datos.
def registrar_paciente(paciente):

    # Se establece la conexión con SQLite.
    conexion = conectar_bd()

    # Se crea el cursor para ejecutar instrucciones SQL.
    cursor = conexion.cursor()

    # Ejecuta la sentencia INSERT.
    cursor.execute("""

        INSERT INTO pacientes
        (nombre, cedula, edad, telefono)

        VALUES (?, ?, ?, ?)

    """, (

        paciente.get_nombre(),

        paciente.get_cedula(),

        paciente.get_edad(),

        paciente.get_telefono()

    ))

    # Guarda los cambios realizados.
    conexion.commit()

    # Cierra la conexión con la base de datos.
    conexion.close()

# CONSULTAR PACIENTES
# ----------------------------------------------------------

# Devuelve todos los pacientes registrados.
def consultar_paciente():

    # Abre la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Ejecuta la consulta SQL.
    cursor.execute("""

        SELECT *

        FROM paciente

        ORDER BY nombre

    """)

    # Guarda todos los registros obtenidos.
    pacientes = cursor.fetchall()

    # Cierra la conexión.
    conexion.close()

    # Devuelve la lista de pacientes.
    return pacientes

# BUSCAR PACIENTE
# ----------------------------------------------------------

# Busca un paciente utilizando su número de cédula.
def buscar_paciente(cedula):

    # Abre la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Ejecuta la consulta.
    cursor.execute("""

        SELECT *

        FROM paciente

        WHERE cedula = ?

    """, (cedula,))

    # Obtiene solamente un registro.
    paciente = cursor.fetchone()

    # Cierra la conexión.
    conexion.close()

    # Devuelve el resultado.
    return paciente

# ACTUALIZAR PACIENTE
# ----------------------------------------------------------

# Actualiza la información de un paciente existente.
def actualizar_paciente(paciente):

    # Abre la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Ejecuta la actualización.
    cursor.execute("""

        UPDATE paciente

        SET

        nombre = ?,

        edad = ?,

        telefono = ?

        WHERE cedula = ?

    """, (

        paciente.get_nombre(),

        paciente.get_edad(),

        paciente.get_telefono(),

        paciente.get_cedula()

    ))

    # Guarda los cambios.
    conexion.commit()

    # Cierra la conexión.
    conexion.close()

# ELIMINAR PACIENTE
# ----------------------------------------------------------

# Elimina un paciente utilizando su cédula.
def eliminar_paciente(cedula):

    # Abre la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Ejecuta la eliminación.
    cursor.execute("""

        DELETE

        FROM paciente

        WHERE cedula = ?

    """, (cedula,))

    # Guarda los cambios.
    conexion.commit()

    # Cierra la conexión.
    conexion.close()

# CONTAR PACIENTES
# ----------------------------------------------------------

# Devuelve la cantidad total de pacientes registrados.
def contar_paciente():

    # Abre la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Cuenta todos los pacientes.
    cursor.execute("""

        SELECT COUNT(*)

        FROM paciente

    """)

    # Obtiene el resultado.
    cantidad = cursor.fetchone()[0]

    # Cierra la conexión.
    conexion.close()

    # Devuelve la cantidad encontrada.
    return cantidad

# REGISTRAR MÉDICO
# ----------------------------------------------------------

# Esta función recibe un objeto Medico y guarda su
# información dentro de la base de datos.
def registrar_medico(medico):

    # Establece la conexión con la base de datos.
    conexion = conectar_bd()

    # Crea el cursor para ejecutar instrucciones SQL.
    cursor = conexion.cursor()

    # Ejecuta la sentencia INSERT.
    cursor.execute("""

        INSERT INTO medico
        (nombre, cedula, especialidad, telefono, consultorio)

        VALUES (?, ?, ?, ?, ?)

    """, (

        medico.get_nombre(),

        medico.get_cedula(),

        medico.get_especialidad(),

        medico.get_telefono(),

        medico.get_consultorio()

    ))

    # Guarda los cambios realizados.
    conexion.commit()

    # Cierra la conexión.
    conexion.close()

# CONSULTAR MÉDICOS
# ----------------------------------------------------------

# Devuelve todos los médicos registrados.
def consultar_medico():

    # Abre la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Ejecuta la consulta SQL.
    cursor.execute("""

        SELECT *

        FROM medico

        ORDER BY nombre

    """)

    # Obtiene todos los registros encontrados.
    medicos = cursor.fetchall()

    # Cierra la conexión.
    conexion.close()

    # Devuelve la lista de médicos.
    return medico

# BUSCAR MÉDICO
# ----------------------------------------------------------

# Busca un médico utilizando su número de cédula.
def buscar_medico(cedula):

    # Abre la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Ejecuta la consulta.
    cursor.execute("""

        SELECT *

        FROM medico

        WHERE cedula = ?

    """, (cedula,))

    # Obtiene un solo registro.
    medico = cursor.fetchone()

    # Cierra la conexión.
    conexion.close()

    # Devuelve el resultado obtenido.
    return medico

# ACTUALIZAR MÉDICO
# ----------------------------------------------------------

# Actualiza la información de un médico existente.
def actualizar_medico(medico):

    # Abre la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Ejecuta la actualización.
    cursor.execute("""

        UPDATE medico

        SET

        nombre = ?,

        especialidad = ?,

        telefono = ?,

        consultorio = ?

        WHERE cedula = ?

    """, (

        medico.get_nombre(),

        medico.get_especialidad(),

        medico.get_telefono(),

        medico.get_consultorio(),

        medico.get_cedula()

    ))

    # Guarda los cambios.
    conexion.commit()

    # Cierra la conexión.
    conexion.close()

# ELIMINAR MÉDICO
# ----------------------------------------------------------

# Elimina un médico utilizando su número de cédula.
def eliminar_medico(cedula):

    # Abre la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Ejecuta la eliminación.
    cursor.execute("""

        DELETE

        FROM medico

        WHERE cedula = ?

    """, (cedula,))

    # Guarda los cambios.
    conexion.commit()

    # Cierra la conexión.
    conexion.close()

# CONTAR MÉDICOS
# ----------------------------------------------------------

# Devuelve la cantidad total de médicos registrados.
def contar_medico():

    # Abre la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Cuenta todos los médicos registrados.
    cursor.execute("""

        SELECT COUNT(*)

        FROM medico

    """)

    # Obtiene el resultado de la consulta.
    cantidad = cursor.fetchone()[0]

    # Cierra la conexión.
    conexion.close()

    # Devuelve la cantidad encontrada.
    return cantidad

# REGISTRAR CITA
# ----------------------------------------------------------

# Esta función recibe un objeto Cita y lo almacena en la
# base de datos.
def registrar_cita(cita):

    # Comprueba que exista el paciente.
    if buscar_paciente(cita.get_id_paciente()) is None:
        return False

    # Comprueba que exista el médico.
    if buscar_medico(cita.get_id_medico()) is None:
        return False

    # Abre la conexión con la base de datos.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Ejecuta la sentencia INSERT.
    cursor.execute("""

        INSERT INTO cita
        (fecha, hora, estado, id_paciente, id_medico)

        VALUES (?, ?, ?, ?, ?)

    """, (

        cita.get_fecha(),

        cita.get_hora(),

        cita.get_estado(),

        cita.get_id_paciente(),

        cita.get_id_medico()

    ))

    # Guarda los cambios.
    conexion.commit()

    # Cierra la conexión.
    conexion.close()

    # Indica que el registro fue exitoso.
    return True

# CONSULTAR CITAS
# ----------------------------------------------------------

# Devuelve todas las citas registradas.
def consultar_citas():

    # Abre la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Consulta las citas junto con el nombre del paciente y
    # del médico mediante un JOIN.
    cursor.execute("""

        SELECT

        citas.id,

        citas.fecha,

        citas.hora,

        citas.estado,

        pacientes.nombre,

        medicos.nombre

        FROM cita

        INNER JOIN paciente

        ON citas.id_paciente = pacientes.id

        INNER JOIN medico

        ON citas.id_medico = medicos.id

        ORDER BY citas.fecha, citas.hora

    """)

    # Obtiene todos los registros.
    citas = cursor.fetchall()

    # Cierra la conexión.
    conexion.close()

    # Devuelve la lista de citas.
    return citas

# BUSCAR CITA
# ----------------------------------------------------------

# Busca una cita utilizando su identificador.
def buscar_cita(id_cita):

    # Abre la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Ejecuta la consulta.
    cursor.execute("""

        SELECT *

        FROM cita

        WHERE id = ?

    """, (id_cita,))

    # Obtiene un único registro.
    cita = cursor.fetchone()

    # Cierra la conexión.
    conexion.close()

    # Devuelve el resultado.
    return cita

# ACTUALIZAR CITA
# ----------------------------------------------------------

# Actualiza la información de una cita existente.
def actualizar_cita(cita):

    # Abre la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Ejecuta la actualización.
    cursor.execute("""

        UPDATE cita

        SET

        fecha = ?,

        hora = ?,

        estado = ?,

        id_paciente = ?,

        id_medico = ?

        WHERE id = ?

    """, (

        cita.get_fecha(),

        cita.get_hora(),

        cita.get_estado(),

        cita.get_id_paciente(),

        cita.get_id_medico(),

        cita.get_id()

    ))

    # Guarda los cambios.
    conexion.commit()

    # Cierra la conexión.
    conexion.close()

# ELIMINAR CITA
# ----------------------------------------------------------

# Elimina una cita utilizando su identificador.
def eliminar_cita(id_cita):

    # Abre la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Ejecuta la eliminación.
    cursor.execute("""

        DELETE

        FROM cita

        WHERE id = ?

    """, (id_cita,))

    # Guarda los cambios.
    conexion.commit()

    # Cierra la conexión.
    conexion.close()

# CONTAR CITAS
# ----------------------------------------------------------

# Devuelve la cantidad total de citas registradas.
def contar_citas():

    # Abre la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Cuenta todas las citas.
    cursor.execute("""

        SELECT COUNT(*)

        FROM cita

    """)

    # Obtiene el resultado.
    cantidad = cursor.fetchone()[0]

    # Cierra la conexión.
    conexion.close()

    # Devuelve la cantidad de citas.
    return cantidad

# REGISTRAR HISTORIAL CLÍNICO
# ----------------------------------------------------------

# Esta función recibe un objeto HistorialClinico y guarda
# su información dentro de la base de datos.
def registrar_historial(historial):

    # Verifica que el paciente exista.
    if buscar_paciente_por_id(historial.get_id_paciente()) is None:
        return False

    # Establece la conexión con SQLite.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Ejecuta la sentencia INSERT.
    cursor.execute("""

        INSERT INTO historial_clinico
        (fecha, diagnostico, tratamiento, id_paciente)

        VALUES (?, ?, ?, ?)

    """, (

        historial.get_fecha(),

        historial.get_diagnostico(),

        historial.get_tratamiento(),

        historial.get_id_paciente()

    ))

    # Guarda los cambios realizados.
    conexion.commit()

    # Cierra la conexión.
    conexion.close()

    # Indica que el registro fue exitoso.
    return True

# CONSULTAR HISTORIALES CLÍNICOS
# ----------------------------------------------------------

# Devuelve todos los historiales registrados.
def consultar_historiales():

    # Establece la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Consulta todos los historiales junto con el nombre
    # del paciente.
    cursor.execute("""

        SELECT

        historial_clinico.id,

        historial_clinico.fecha,

        historial_clinico.diagnostico,

        historial_clinico.tratamiento,

        pacientes.nombre

        FROM historial_clinico

        INNER JOIN paciente

        ON historial_clinico.id_paciente = pacientes.id

        ORDER BY historial_clinico.fecha DESC

    """)

    # Obtiene todos los registros.
    historiales = cursor.fetchall()

    # Cierra la conexión.
    conexion.close()

    # Devuelve la lista obtenida.
    return historiales

# BUSCAR HISTORIAL CLÍNICO
# ----------------------------------------------------------

# Busca un historial clínico mediante su identificador.
def buscar_historial(id_historial):

    # Establece la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Ejecuta la consulta.
    cursor.execute("""

        SELECT *

        FROM historial_clinico

        WHERE id = ?

    """, (id_historial,))

    # Obtiene un solo registro.
    historial = cursor.fetchone()

    # Cierra la conexión.
    conexion.close()

    # Devuelve el historial encontrado.
    return historial

# ACTUALIZAR HISTORIAL CLÍNICO
# ----------------------------------------------------------

# Actualiza la información de un historial clínico.
def actualizar_historial(historial):

    # Establece la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Ejecuta la actualización.
    cursor.execute("""

        UPDATE historial_clinico

        SET

        fecha = ?,

        diagnostico = ?,

        tratamiento = ?,

        id_paciente = ?

        WHERE id = ?

    """, (

        historial.get_fecha(),

        historial.get_diagnostico(),

        historial.get_tratamiento(),

        historial.get_id_paciente(),

        historial.get_id()

    ))

    # Guarda los cambios.
    conexion.commit()

    # Cierra la conexión.
    conexion.close()

# Devuelve el ID del paciente
    def get_id_paciente(self):
        return self.__id_paciente
# Devuelve el identificador del historial clínico.
    def get_id(self):
        return self.__id_historial

# ELIMINAR HISTORIAL CLÍNICO
# ----------------------------------------------------------

# Elimina un historial clínico mediante su identificador.
def eliminar_historial(id_historial):

    # Establece la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Ejecuta la sentencia DELETE.
    cursor.execute("""

        DELETE

        FROM historial_clinico

        WHERE id = ?

    """, (id_historial,))

    # Guarda los cambios.
    conexion.commit()

    # Cierra la conexión.
    conexion.close()

# CONTAR HISTORIALES CLÍNICOS
# ----------------------------------------------------------

# Devuelve la cantidad total de historiales clínicos.
def contar_historiales():

    # Establece la conexión.
    conexion = conectar_bd()

    # Crea el cursor.
    cursor = conexion.cursor()

    # Cuenta todos los historiales.
    cursor.execute("""

        SELECT COUNT(*)

        FROM historial_clinico

    """)

    # Obtiene el resultado.
    cantidad = cursor.fetchone()[0]

    # Cierra la conexión.
    conexion.close()

    # Devuelve la cantidad encontrada.
    return cantidad
# ==========================================================
# INTERFAZ GRAFICA
# ==========================================================
# Crea la ventana principal del sistema
ventana = Tk()

# Asigna el título que aparecerá en la barra superior
ventana.title("Sistema de Gestión de Citas Médicas")

# Define el ancho y alto de la ventana
ventana.geometry("850x600")

# Impide que el usuario cambie el tamaño de la ventana
ventana.resizable(False, False)

# Cambia el color de fondo de la ventana
ventana.configure(bg="#EAF4FC")

# Muestra el nombre del sistema.
titulo = Label(

    ventana,

    text="SISTEMA DE GESTIÓN DE CITAS MÉDICAS",

    font=("Arial", 20, "bold"),

    bg="#EAF4FC",

    fg="#003366"

)

# Coloca el título en la ventana.
titulo.pack(pady=20)

# Crea un Frame para organizar todos los botones del menú.
frame_botones = Frame(

    ventana,

    bg="#EAF4FC"

)

# Coloca el Frame en la ventana.
frame_botones.pack(pady=35)

# Este botón abrirá la ventana de administración
# de pacientes.
btn_pacientes = Button(

    frame_botones,

    text="👤 Pacientes",

    width=25,

    height=2,

    font=("Arial", 11, "bold"),

    command=lambda: abrir_ventana_pacientes()

)

# Coloca el botón en pantalla.
btn_pacientes.pack(pady=6)

# Este botón abrirá la ventana de administración
# de médicos.
btn_medicos = Button(

    frame_botones,

    text="🩺 Médicos",

    width=25,

    height=2,

    font=("Arial", 11, "bold"),

    command=lambda: abrir_ventana_medicos()

)

# Coloca el botón.
btn_medicos.pack(pady=6)

# Este botón permitirá administrar las citas médicas.
btn_citas = Button(

    frame_botones,

    text="📅 Citas Médicas",

    width=25,

    height=2,

    font=("Arial", 11, "bold"),

    command=lambda: abrir_ventana_citas()

)

# Coloca el botón.
btn_citas.pack(pady=6)

# Este botón abrirá la ventana del historial clínico.
btn_historial = Button(

    frame_botones,

    text="📋 Historial Clínico",

    width=25,

    height=2,

    font=("Arial", 11, "bold"),

    command=lambda: abrir_ventana_historial()

)

# Coloca el botón.
btn_historial.pack(pady=6)

# Este botón administrará la cola de espera.
btn_cola = Button(

    frame_botones,

    text="⏳ Sala de Espera",

    width=25,

    height=2,

    font=("Arial", 11, "bold"),

    command=lambda: abrir_ventana_cola()

)

# Coloca el botón.
btn_cola.pack(pady=6)

# Este botón mostrará información general del sistema.
btn_estadisticas = Button(

    frame_botones,

    text="📊 Estadísticas",

    width=25,

    height=2,

    font=("Arial", 11, "bold"),

    command=lambda: abrir_ventana_estadisticas()

)

# Coloca el botón.
btn_estadisticas.pack(pady=6)

# Este botón finaliza la ejecución del sistema.
btn_salir = Button(

    frame_botones,

    text="Salir",

    width=25,

    height=2,

    bg="#C62828",

    fg="white",

    font=("Arial", 11, "bold"),

    command=ventana.destroy

)

# Coloca el botón.
btn_salir.pack(pady=12)

# Inicia el ciclo principal de la interfaz gráfica.
ventana.mainloop()

# Esta función crea la ventana donde se administrarán
# todos los pacientes del sistema.
def abrir_ventana_pacientes():

    # Crea una nueva ventana independiente.
    ventana_pacientes = Toplevel()

    # Asigna el título de la ventana.
    ventana_pacientes.title("Administración de Pacientes")

    # Define el tamaño de la ventana.
    ventana_pacientes.geometry("900x650")

    # Impide modificar el tamaño.
    ventana_pacientes.resizable(False, False)

    # Cambia el color de fondo.
    ventana_pacientes.configure(bg="#EAF4FC")

# Muestra el nombre de la ventana.
    Label(

        ventana_pacientes,

        text="REGISTRO DE PACIENTES",

        font=("Arial",18,"bold"),

        bg="#EAF4FC",

        fg="#003366"

    ).pack(pady=15)

# Contendrá todos los campos del formulario.
    frame_datos = Frame(

        ventana_pacientes,

        bg="#EAF4FC"

    )

    frame_datos.pack(pady=10)

Label(

        frame_datos,

        text="Nombre:",

        font=("Arial",11),

        bg="#EAF4FC"

    ).grid(row=0,column=0,padx=10,pady=8,sticky="e")

    entry_nombre = Entry(

        frame_datos,

        width=35

    )

    entry_nombre.grid(row=0,column=1,pady=8)

Label(

        frame_datos,

        text="Cédula:",

        font=("Arial",11),

        bg="#EAF4FC"

    ).grid(row=1,column=0,padx=10,pady=8,sticky="e")

    entry_cedula = Entry(

        frame_datos,

        width=35

    )

    entry_cedula.grid(row=1,column=1,pady=8)

Label(

        frame_datos,

        text="Edad:",

        font=("Arial",11),

        bg="#EAF4FC"

    ).grid(row=2,column=0,padx=10,pady=8,sticky="e")

    entry_edad = Entry(

        frame_datos,

        width=35

    )

    entry_edad.grid(row=2,column=1,pady=8)

Label(

        frame_datos,

        text="Teléfono:",

        font=("Arial",11),

        bg="#EAF4FC"

    ).grid(row=3,column=0,padx=10,pady=8,sticky="e")

    entry_telefono = Entry(

        frame_datos,

        width=35

    )

    entry_telefono.grid(row=3,column=1,pady=8)

# Agrupa todos los botones del formulario.
    frame_botones = Frame(

        ventana_pacientes,

        bg="#EAF4FC"

    )

    frame_botones.pack(pady=15)

 Button(

        frame_botones,

        text="Registrar",

        width=12

    ).grid(row=0,column=0,padx=5)

    # ------------------------------------------------------
    # BOTÓN BUSCAR
    # ------------------------------------------------------

    Button(

        frame_botones,

        text="Buscar",

        width=12

    ).grid(row=0,column=1,padx=5)

    # ------------------------------------------------------
    # BOTÓN ACTUALIZAR
    # ------------------------------------------------------

    Button(

        frame_botones,

        text="Actualizar",

        width=12

    ).grid(row=0,column=2,padx=5)

    # ------------------------------------------------------
    # BOTÓN ELIMINAR
    # ------------------------------------------------------

    Button(

        frame_botones,

        text="Eliminar",

        width=12

    ).grid(row=0,column=3,padx=5)

    # ------------------------------------------------------
    # BOTÓN LIMPIAR
    # ------------------------------------------------------

    Button(

        frame_botones,

        text="Limpiar",

        width=12

    ).grid(row=0,column=4,padx=5)

    # ------------------------------------------------------
    # BOTÓN CERRAR
    # ------------------------------------------------------

    Button(

        frame_botones,

        text="Cerrar",

        width=12,

        command=ventana_pacientes.destroy

    ).grid(row=0,column=5,padx=5)

# Crea la tabla donde se mostrarán los pacientes.
    tabla = ttk.Treeview(

        ventana_pacientes,

        columns=("ID","Nombre","Cedula","Edad","Telefono"),

        show="headings",

        height=12

    )

    tabla.heading("ID",text="ID")
    tabla.heading("Nombre",text="Nombre")
    tabla.heading("Cedula",text="Cédula")
    tabla.heading("Edad",text="Edad")
    tabla.heading("Telefono",text="Teléfono")

    tabla.column("ID",width=50,anchor="center")
    tabla.column("Nombre",width=220)
    tabla.column("Cedula",width=150)
    tabla.column("Edad",width=80,anchor="center")
    tabla.column("Telefono",width=150)

    tabla.pack(pady=20)
