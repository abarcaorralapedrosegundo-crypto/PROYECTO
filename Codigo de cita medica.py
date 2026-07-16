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

# CONFIGURACIÓN DE LA BASE DE DATOS
# ==========================================================

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
# Crea la ventana principal del programa
ventana = Tk()

ventana.title("Sistema de Citas Médicas")  # Coloca un título en la barra superior de la ventana
ventana.geometry("400x250")  # Define el tamaño de la ventana (ancho x alto)

# Crea un texto de bienvenida y lo coloca en la ventana
Label(ventana, text="Sistema de Gestión de Citas Médicas").pack(pady=15)

# Crea un botón para registrar pacientes
Button(ventana, text="Registrar Paciente").pack(pady=5)

# Crea un botón para consultar los pacientes registrados
Button(ventana, text="Consultar Pacientes").pack(pady=5)

# Crea un botón para agendar una cita médica
Button(ventana, text="Agendar Cita").pack(pady=5)

# Crea un botón para cerrar la aplicación
Button(ventana, text="Salir", command=ventana.destroy).pack(pady=15)

ventana.mainloop()  # Mantiene la ventana abierta hasta que el usuario la cierre
