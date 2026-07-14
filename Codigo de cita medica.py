'''Grupo: 2
Integrantes: Abarca Orrala Pedro Segundo, Delacruz Castillo Henry Alexander, 
Lopez Mendoza Genessis Milena, Piedra Ortega Francisco Andres, 
Quinde Eugenio Julexi Tatiana'''
# Librerías
import os
import sqlite3  # Importa la librería sqlite3 para trabajar con bases de datos SQLite
from collections import deque  # Importa la estructura deque,que se utilizará como una cola (FIFO)
from tkinter import *  # Importa todos los componentes de Tkinter para crear la interfaz gráfica

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

    # Método para registrar un paciente
    def registrar(self):
        print("Paciente registrado correctamente.")

    # Método para actualizar un paciente
    def actualizar(self):
        print("Paciente actualizado correctamente.")

    # Método para consultar el historial
    def consultar_historial(self):
        print("Consultando historial clínico...")

# La clase Medico hereda de Persona.
class Medico(Persona):

    # Constructor.
    def _init_(self, id_medico, nombre, cedula,
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

    # Métodos Get.

    def get_id(self):
        return self.__id_medico

    def get_especialidad(self):
        return self.__especialidad

    def get_telefono(self):
        return self.__telefono

    def get_consultorio(self):
        return self.__consultorio

    # Método registrar.
    def registrar(self):
        print("Médico registrado correctamente.")

    # Método consultar agenda.
    def consultar_agenda(self):
        print("Consultando agenda del médico...")

# Representa una cita médica.
class Cita:

    # Constructor.
    def __init__(self, id_cita, fecha, hora, estado):

        # Guarda el ID.
        self.__id_cita = id_cita # Guarda el ID de la cita como un atributo privado

        # Guarda la fecha.
        self.__fecha = fecha # Guarda la fecha de la cita como un atributo privado

        # Guarda la hora.
        self.__hora = hora # Guarda la hora de la cita como un atributo privado

        # Guarda el estado.
        self.__estado = estado # Guarda el estado de la cita como un atributo privado

    # Métodos Get.

    def get_fecha(self):
        return self.__fecha # Devuelve la fecha de la cita

    def get_hora(self):
        return self.__hora # Devuelve la hora de la cita

    def get_estado(self):
        return self.__estado # Devuelve el estado de la cita

    # Agenda una cita.
    def agendar(self): 
        print("Cita agendada correctamente.")

    # Cancela una cita.
    def cancelar(self):
        print("Cita cancelada.")

    # Reprograma una cita.
    def reprogramar(self):
        print("Cita reprogramada.")

# Representa el historial de un paciente.
class HistorialClinico:

    # Constructor.
    def __init__(self, id_historial, fecha,
                 diagnostico, tratamiento): #Constructor de la clase.Se ejecuta automáticamente al crear un objeto.

        # Guarda el ID.
        self.__id_historial = id_historial # Guarda el ID del historial clínico como un atributo privado

        # Guarda la fecha.
        self.__fecha = fecha # Guarda la fecha del historial clínico como un atributo privado

        # Guarda el diagnóstico.
        self.__diagnostico = diagnostico # Guarda el diagnóstico del historial clínico como un atributo privado

        # Guarda el tratamiento.
        self.__tratamiento = tratamiento # Guarda el tratamiento del historial clínico como un atributo privado

    # Agrega un registro.
    def agregar_registro(self):
        print("Registro agregado.")

    # Consulta el historial.
    def consultar(self):
        print("Mostrando historial...")

# ===========================================
# ESTRUCTURA DE DATOS
# ===========================================
# Crea una cola vacía
cola_espera = deque()

# Función para ingresar un paciente
def ingresar_cola(nombre):

    # Agrega el paciente al final
    cola_espera.append(nombre)

    print(nombre, "ingresó a la sala de espera")

# Función para atender.
def atender_paciente():

    # Verifica que existan pacientes
    if cola_espera:
        paciente = cola_espera.popleft()  # Extrae el primero
        print("Atendiendo a:", paciente)
    else:
        print("No existen pacientes en espera")
# ===========================================
# BASE DE DATOS
# ===========================================

# PASO 1: Conectar con la base de datos
conexion = sqlite3.connect("clinica.db")  # Si el archivo no existe,SQLite lo crea automáticamente

# PASO 2: Crear el cursor para ejecutar instrucciones SQL
cursor = conexion.cursor()

# PASO 3: Crear la tabla de pacientes si todavía no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS pacientes(

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    cedula TEXT,
    edad INTEGER,
    telefono TEXT

)
""")

# PASO 4: Insertar el primer paciente en la base de datos
cursor.execute(
    "INSERT INTO pacientes(nombre,cedula,edad,telefono) VALUES (?,?,?,?)",
    ("Pedro Vera","0954789652",21,"0984697459")  # Valores que se guardarán en la tabla
)

# Insertar el segundo paciente
cursor.execute(
    "INSERT INTO pacientes(nombre,cedula,edad,telefono) VALUES (?,?,?,?)",
    ("María López","0912345678",30,"0914795672")  # Valores que se guardarán en la tabla
)

# Insertar el tercer paciente
cursor.execute(
    "INSERT INTO pacientes(nombre,cedula,edad,telefono) VALUES (?,?,?,?)",
    ("Carlos Pizarro","0985867412",20,"0974965178")  # Valores que se guardarán en la tabla
)
# PASO 5: Guardar todos los cambios realizados en la base de datos
conexion.commit()

# PASO 6: Consultar todos los registros de la tabla pacientes
cursor.execute("SELECT * FROM pacientes")

# PASO 7: Obtener todos los registros encontrados
resultados = cursor.fetchall()

print("PACIENTES REGISTRADOS")  # Mostrar un título en la consola

# PASO 8: Reocrrer cada registro obtenido y mostrarlo
for fila in resultados:
    print(fila)

# PASO 9: Cerrar la conexión con la base de datos
conexion.close()

# ===========================================
# INTERFAZ GRÁFICA
# ===========================================

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
