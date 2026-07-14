'''Grupo: 2
Integrantes: Abarca Orrala Pedro Segundo, Delacruz Castillo Henry Alexander, 
Lopez Mendoza Genessis Milena, Piedra Ortega Francisco Andres, 
Quinde Eugenio Julexi Tatiana'''
# Librerías
import sqlite3  # Importa la librería sqlite3 para trabajar con bases de datos SQLite
from collections import deque  # Importa la estructura deque,que se utilizará como una cola (FIFO)
from tkinter import *  # Importa todos los componentes de Tkinter para crear la interfaz gráfica

# ===========================================
# CLASE DEL DOMINIO
# ===========================================

# Se crea la clase Paciente para representar a cada paciente del sistema
class Paciente:

    def __init__(self, nombre, cedula, edad, telefono):  #Constructor de la clase.Se ejecuta automáticamente al crear un objeto
        self.__nombre = nombre  # Guarda el nombre del paciente como un atributo privado
        self.__cedula = cedula  # Guarda la cédula del paciente como un atributo privado
        self.__edad = edad  # Guarda la edad del paciente como un atributo privado
        self.__telefono = telefono  # Guarda el telefono del paciente como un atributo privado

    # Método que devuelve el nombre del paciente
    def get_nombre(self):
        return self.__nombre

    # Método que devuelve la cédula del paciente
    def get_cedula(self):
        return self.__cedula

    # Método que devuelve la edad del paciente
    def get_edad(self):
        return self.__edad
    
    # Método que devuelve el teléfono del paciente
    def get_telefono(self):
        return self.__telefono

    # Método que muestra los datos del paciente en la consola
    def mostrar_datos(self):
        print("Nombre:", self.__nombre)
        print("Cédula:", self.__cedula)
        print("Edad:", self.__edad)
        print("Teléfono:", self.__telefono)

# ===========================================
# ESTRUCTURA DE DATOS
# ===========================================

# Se crea una cola vacía para almacenar los pacientes en espera
cola_espera = deque()

cola_espera.append("Pedro Vera")  # Agrega un paciente al final de la cola
cola_espera.append("María López")  #Agrega otro paciente al final de la cola
cola_espera.append("Carlos Pizarro")  # Agrega un tercer paciente al final de la cola

# Extrae y muestra el primer paciente de la cola
print("Siguiente paciente:", cola_espera.popleft())

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