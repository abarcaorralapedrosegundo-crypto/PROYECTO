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

lista_citas = []  # Pila donde se almacenan los historiales clínicos

# ===========================================
# CLASE DEL DOMINIO
# ===========================================

# Se crea la clase Persona para representar la información
# común que tendrán pacientes y médicos.
class Persona:
    # Constructor de la clase Persona.
    # Se ejecuta automáticamente cuando se crea un objeto.
    def __init__(self, nombre, cedula,telefono):
        self.__nombre = nombre  # Guarda el nombre como un atributo privado
        self.__cedula = cedula  # Guarda la cédula como un atributo privado
        self.__telefono = telefono  # Guarda el telefono como un atributo privado
    def get_nombre(self):
        return self.__nombre  # Devuelve el nombre
    
    def get_cedula(self):
        return self.__cedula  # Devuelve la cédula

    def get_telefono(self):
        return self.__telefono  # Devuelve el telefono
    
    # Permite modificar el nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Permite modificar la cédula
    def set_cedula(self, cedula):
        self.__cedula = cedula

    # Permite modificar el telefono
    def set_telefono(self, telefono):
        self.__telefono = telefono
        
    # Muestra los datos de la persona
    def mostrar_datos(self):
        print("Nombre:", self.__nombre)
        print("Cédula:", self.__cedula)
        print("Teléfono:", self.__telefono)

# La clase Paciente hereda los atributos y métodos
# de la clase Persona
class Paciente(Persona):

    # Constructor de la clase Paciente
    def __init__(self, id_paciente,nombre, cedula,telefono,edad):
        super().__init__(nombre, cedula,telefono)   # Llama al constructor de la clase Persona
        self.__id_paciente = id_paciente  # Guarda el identificador del paciente
        self.__edad = edad  # Guarda la edad

    # Devuelve el ID
    def get_id_paciente(self):
        return self.__id_paciente
    
    # Devuelve la edad
    def get_edad(self):
        return self.__edad
    
    # Permite modificar la edad
    def set_edad(self, edad):
        self.__edad = edad

    # Muestra toda la información del paciente
    def mostrar_datos(self):

        print("ID:", self.__id_paciente)

        print("Nombre:", self.get_nombre())

        print("Cédula:", self.get_cedula())

        print("Edad:", self.__edad)

        print("Teléfono:", self.get_telefono())

# La clase Medico hereda de Persona
class Medico(Persona):

    # Constructor
    def __init__(self, id_medico,nombre, cedula,telefono,especialidad,consultorio):

        # Llama al constructor de Persona.
        super().__init__(nombre, cedula,telefono)

        # Guarda el ID
        self.__id_medico = id_medico

        # Guarda la especialidad.
        self.__especialidad = especialidad

        # Guarda el consultorio.
        self.__consultorio = consultorio

    # Métodos Get y Devuelve el ID
    def get_id_medico(self):
        return self.__id_medico

    def get_especialidad(self):
        return self.__especialidad

    def get_consultorio(self):
        return self.__consultorio

    # Permite modificar la especialidad
    def set_especialidad(self, especialidad):
        self.__especialidad = especialidad

    # Permite modificar el consultorio
    def set_consultorio(self, consultorio):
        self.__consultorio = consultorio

    # Muestra la información del médico
    def mostrar_datos(self):

        print("ID:", self.__id_medico)

        print("Nombre:", self.get_nombre())

        print("Cédula:", self.get_cedula())

        print("Especialidad:", self.__especialidad)

        print("Teléfono:", self.get_telefono())

        print("Consultorio:", self.__consultorio)

# Representa una cita médica
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
    def get_id_cita(self):
        return self.__id_cita  # Devuelve el id de cita
    
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

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_hora(self, hora):
        self.__hora = hora

    def set_estado(self, estado):
        self.__estado = estado
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
                     
    def get_id_historial(self):
        return self.__id_historial
    
    # Devuelve el ID del paciente
    def get_id_paciente(self):
        return self.__id_paciente
        
    # Devuelve la fecha
    def get_fecha(self):
        return self.__fecha

    # Devuelve el diagnóstico
    def get_diagnostico(self):
        return self.__diagnostico

    # Devuelve el tratamiento
    def get_tratamiento(self):
        return self.__tratamiento

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_diagnostico(self, diagnostico):
        self.__diagnostico = diagnostico

    def set_tratamiento(self, tratamiento):
        self.__tratamiento = tratamiento
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

# Agrega una cita a la lista.
def agregar_cita(cita):

    # Guarda la cita en la lista
    lista_citas.append(cita)

# Devuelve todas las citas registradas
def mostrar_citas():

    # Devuelve la lista completa
    return lista_citas
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
    
    # Crea la tabla de paciente
    cursor.execute("""

        CREATE TABLE IF NOT EXISTS paciente(

            id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL,

            cedula TEXT UNIQUE NOT NULL,

            edad INTEGER NOT NULL,

            telefono TEXT NOT NULL

        )

    """)

# Crea la tabla de médico
    cursor.execute("""

        CREATE TABLE IF NOT EXISTS medico(

            id_medico INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL,

            cedula TEXT UNIQUE NOT NULL,

            especialidad TEXT NOT NULL,

            telefono TEXT NOT NULL,

            consultorio TEXT NOT NULL

        )

    """)

# Crea la tabla donde se almacenarán todas las cita
    cursor.execute("""

        CREATE TABLE IF NOT EXISTS cita(

            id_cita INTEGER PRIMARY KEY AUTOINCREMENT,

            fecha TEXT NOT NULL,

            hora TEXT NOT NULL,

            estado TEXT NOT NULL,

            id_paciente INTEGER NOT NULL,

            id_medico INTEGER NOT NULL,

            FOREIGN KEY(id_paciente) REFERENCES paciente(id),

            FOREIGN KEY(id_medico) REFERENCES medico(id)

        )

    """)
    # Crea la tabla del historial clínico
    cursor.execute("""

        CREATE TABLE IF NOT EXISTS historial_clinico(

            id_historial INTEGER PRIMARY KEY AUTOINCREMENT,

            fecha TEXT NOT NULL,

            diagnostico TEXT NOT NULL,

            tratamiento TEXT NOT NULL,

            id_paciente INTEGER NOT NULL,

            FOREIGN KEY(id_paciente) REFERENCES paciente(id)

        )

    """)
    # GUARDAR LOS CAMBIOS
    # ------------------------------------------------------

    # Guarda todas las tablas creadas.
    conexion.commit()

    # Cierra la conexión.
    conexion.close()
    # Cuando el programa inicie se crearán automáticamente
# todas las tablas del sistema
crear_tablas()

# ===========================================
# FUNCIONES DEL SISTEMA
# ===========================================
# Esta función registra un nuevo paciente en la base de datos.
def registrar_paciente(nombre, cedula, edad, telefono):
    # Verifica que todos los campos tengan información.
if nombre == "" or cedula == "" or edad == "" or telefono == "":

    # Muestra un mensaje de advertencia.
    messagebox.showwarning(
        "Campos vacíos",
        "Complete todos los datos del paciente."
    )

    # Finaliza la función sin guardar información.
    return
    
    # Establece la conexión con la base de datos.
    conexion = conectar_bd()

    # Crea un cursor para ejecutar instrucciones SQL.
    cursor = conexion.cursor()

    # Ejecuta la consulta para insertar un nuevo paciente.
    cursor.execute(
        """
        INSERT INTO paciente(nombre, cedula, edad, telefono)
        VALUES(?, ?, ?, ?)
        """,
        (nombre, cedula, edad, telefono)
    )

    # Guarda los cambios realizados en la base de datos.
    conexion.commit()

    # Cierra la conexión con la base de datos.
    conexion.close()

    # Agrega el nombre del paciente a la cola de espera.
    ingresar_cola(nombre)

    # Muestra un mensaje indicando que el registro fue exitoso.
    messagebox.showinfo(
        "Registro exitoso",
        "Paciente registrado correctamente."
    )

# Esta función obtiene todos los pacientes registrados.
def consultar_pacientes():

    # Establece la conexión con la base de datos.
    conexion = conectar_bd()

    # Crea un cursor para ejecutar instrucciones SQL.
    cursor = conexion.cursor()

    # Ejecuta la consulta para obtener todos los pacientes.
    cursor.execute("""
        SELECT * FROM paciente
    """)

    # Guarda todos los registros obtenidos.
    pacientes = cursor.fetchall()

    # Cierra la conexión con la base de datos.
    conexion.close()

    # Devuelve la lista de pacientes.
    return pacientes

# Esta función registra un nuevo médico en la base de datos.
def registrar_medico(nombre, cedula, especialidad, telefono, consultorio):

    # Verifica que todos los campos tengan información.
    if nombre == "" or cedula == "" or especialidad == "" or telefono == "" or consultorio == "":

        # Muestra un mensaje indicando que existen campos vacíos.
        messagebox.showwarning(
            "Campos vacíos",
            "Complete todos los datos del médico."
        )

        # Finaliza la función.
        return

    # Establece la conexión con la base de datos.
    conexion = conectar_bd()

    # Crea un cursor para ejecutar instrucciones SQL.
    cursor = conexion.cursor()

    # Ejecuta la consulta para registrar un nuevo médico.
    cursor.execute(
        """
        INSERT INTO medico(nombre, cedula, especialidad, telefono, consultorio)
        VALUES(?, ?, ?, ?, ?)
        """,
        (nombre, cedula, especialidad, telefono, consultorio)
    )

    # Guarda los cambios realizados en la base de datos.
    conexion.commit()

    # Cierra la conexión con la base de datos.
    conexion.close()

    # Muestra un mensaje indicando que el registro fue exitoso.
    messagebox.showinfo(
        "Registro exitoso",
        "Médico registrado correctamente."
    )

# Esta función obtiene todos los médicos registrados.
def consultar_medicos():

    # Establece la conexión con la base de datos.
    conexion = conectar_bd()

    # Crea un cursor para ejecutar instrucciones SQL.
    cursor = conexion.cursor()

    # Ejecuta la consulta para obtener todos los médicos.
    cursor.execute("""
        SELECT * FROM medico
    """)

    # Guarda todos los registros obtenidos.
    medicos = cursor.fetchall()

    # Cierra la conexión con la base de datos.
    conexion.close()

    # Devuelve la lista de médicos.
    return medicos

# Esta función registra una nueva cita médica.
def registrar_cita(fecha, hora, estado, id_paciente, id_medico):

    # Verifica que todos los campos tengan información.
    if fecha == "" or hora == "" or estado == "" or id_paciente == "" or id_medico == "":

        # Muestra un mensaje indicando que existen campos vacíos.
        messagebox.showwarning(
            "Campos vacíos",
            "Complete todos los datos de la cita."
        )

        # Finaliza la función.
        return

    # Establece la conexión con la base de datos.
    conexion = conectar_bd()

    # Crea un cursor para ejecutar instrucciones SQL.
    cursor = conexion.cursor()

    # Ejecuta la consulta para registrar una nueva cita.
    cursor.execute(
        """
        INSERT INTO cita(fecha, hora, estado, id_paciente, id_medico)
        VALUES(?, ?, ?, ?, ?)
        """,
        (fecha, hora, estado, id_paciente, id_medico)
    )

    # Guarda los cambios realizados en la base de datos.
    conexion.commit()

    # Cierra la conexión con la base de datos.
    conexion.close()

    # Agrega la cita a la lista de citas del sistema.
    agregar_cita(fecha + " - " + hora)

    # Muestra un mensaje indicando que el registro fue exitoso.
    messagebox.showinfo(
        "Registro exitoso",
        "Cita registrada correctamente."
    )

# ===========================================
# INTERFAZ GRÁFICA
# ===========================================

