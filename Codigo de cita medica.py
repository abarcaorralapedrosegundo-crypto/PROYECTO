'''Grupo: 2
Integrantes: Abarca Orrala Pedro Segundo, Delacruz Castillo Henry Alexander, 
Lopez Mendoza Genessis Milena, Piedra Ortega Francisco Andres, 
Quinde Eugenio Julexi Tatiana'''
# Librerías
import sqlite3  # Importa la librería sqlite3 para trabajar con bases de datos SQLite
from collections import deque  # Importa la estructura deque,que se utilizará como una cola (FIFO)
from tkinter import *  # Importa todos los componentes de Tkinter para crear la interfaz gráfica
from tkinter import messagebox

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

# Se crea una cola vacía para almacenar los pacientes en espera
cola_espera = deque()

cola_espera.append("Pedro Vera")  # Agrega un paciente al final de la cola
cola_espera.append("María López")  #Agrega otro paciente al final de la cola
cola_espera.append("Carlos Pizarro")  # Agrega un tercer paciente al final de la cola

# Extrae y muestra el primer paciente de la cola
print("Siguiente paciente:", cola_espera.popleft())

pila_historial = []

pila_historial.append("Diagnóstico 1")
pila_historial.append("Diagnóstico 2")
pila_historial.append("Diagnóstico 3")

print(pila_historial.pop())

lista_citas = []

lista_citas.append("Cita 1")
lista_citas.append("Cita 2")
lista_citas.append("Cita 3")

for cita in lista_citas:
    print(cita)

pacientes = [
    "Pedro",
    "Maria",
    "Carlos"
]

buscar = "Carlos"

for paciente in pacientes:

    if paciente == buscar:

        print("Paciente encontrado")
# ===========================================
# BASE DE DATOS
# ===========================================

# PASO 1: Conectar con la base de datos
conexion = sqlite3.connect("clinica.db")  # Si el archivo no existe,SQLite lo crea automáticamente

# PASO 2: Crear el cursor para ejecutar instrucciones SQL
cursor = conexion.cursor()

# PASO 3: Creacion de las tablas si todavía no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS paciente(

        id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,

        nombre TEXT NOT NULL,

        cedula TEXT UNIQUE NOT NULL,

        edad INTEGER NOT NULL,

        telefono TEXT NOT NULL

    )

    """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS medico(

        id_medico INTEGER PRIMARY KEY AUTOINCREMENT,

        nombre TEXT NOT NULL,

        especialidad TEXT NOT NULL,

        telefono TEXT NOT NULL,

        consultorio TEXT NOT NULL

    )
    """)
    
    # -----------------------------------------------------
    # TABLA CITA
    # -----------------------------------------------------

cursor.execute("""

    CREATE TABLE IF NOT EXISTS cita(

        id_cita INTEGER PRIMARY KEY AUTOINCREMENT,

        fecha TEXT NOT NULL,

        hora TEXT NOT NULL,

        estado TEXT NOT NULL,

        id_paciente INTEGER,

        id_medico INTEGER,

        FOREIGN KEY(id_paciente) REFERENCES paciente(id_paciente),

        FOREIGN KEY(id_medico) REFERENCES medico(id_medico)

    )

    """)

    # -----------------------------------------------------
    # TABLA HISTORIAL CLINICO
    # -----------------------------------------------------

cursor.execute("""

    CREATE TABLE IF NOT EXISTS historial_clinico(

        id_historial INTEGER PRIMARY KEY AUTOINCREMENT,

        fecha TEXT NOT NULL,

        diagnostico TEXT NOT NULL,

        tratamiento TEXT NOT NULL,

        id_paciente INTEGER,

        FOREIGN KEY(id_paciente) REFERENCES paciente(id_paciente)

    )

    """)
# PASO 4: Insertar el primer paciente en la base de datos

    # -----------------------------
    # PACIENTES
    # -----------------------------

cursor.execute(
    """
    INSERT OR IGNORE INTO paciente(nombre,cedula,edad,telefono)
    VALUES(?,?,?,?)
    """,
    ("Pedro Vera","0954789652",21,"0984697459")
)

cursor.execute(
    """
    INSERT OR IGNORE INTO paciente(nombre,cedula,edad,telefono)
    VALUES(?,?,?,?)
    """,
    ("María López","0912345678",30,"0914795672")
)

# Inserta el tercer paciente.
cursor.execute(
    """
    INSERT OR IGNORE INTO paciente(nombre,cedula,edad,telefono)
    VALUES(?,?,?,?)
    """,
    ("Carlos Pizarro","0985867412",20,"0974965178")
)

    # -----------------------------
    # MEDICOS
    # -----------------------------

cursor.execute(
    """
    INSERT OR IGNORE INTO medico(nombre,especialidad,telefono,consultorio)
    VALUES(?,?,?,?)
    """,
    ("Carlos Mora","Cardiología","0981111111","101")
)

cursor.execute(
    """
    INSERT OR IGNORE INTO medico(nombre,especialidad,telefono,consultorio)
    VALUES(?,?,?,?)
    """,
    ("Ana Torres","Pediatría","0982222222","102")
)

cursor.execute(
    """
    INSERT OR IGNORE INTO medico(nombre,especialidad,telefono,consultorio)
    VALUES(?,?,?,?)
    """,
    ("Luis Gómez","Dermatología","0983333333","103")
)

    # -----------------------------
    # CITAS
    # -----------------------------

cursor.execute(
    """
    INSERT OR IGNORE INTO cita(fecha,hora,estado,id_paciente,id_medico)
    VALUES(?,?,?,?,?)
    """,
    ("20/07/2026","08:00","Pendiente",1,1)
)

cursor.execute(
    """
    INSERT OR IGNORE INTO cita(fecha,hora,estado,id_paciente,id_medico)
    VALUES(?,?,?,?,?)
    """,
    ("21/07/2026","09:00","Atendida",2,2)
)

cursor.execute(
    """
    INSERT OR IGNORE INTO cita(fecha,hora,estado,id_paciente,id_medico)
    VALUES(?,?,?,?,?)
    """,
    ("22/07/2026","10:30","Pendiente",3,3)
)

    # -----------------------------
    # HISTORIAL CLINICO
    # -----------------------------

cursor.execute(
    """
    INSERT OR IGNORE INTO historial_clinico(fecha,diagnostico,tratamiento,id_paciente)
    VALUES(?,?,?,?)
    """,
    ("20/07/2026","Gripe","Paracetamol",1)
)

cursor.execute(
    """
    INSERT OR IGNORE INTO historial_clinico(fecha,diagnostico,tratamiento,id_paciente)
    VALUES(?,?,?,?)
    """,
    ("21/07/2026","Migraña","Ibuprofeno",2)
)

cursor.execute(
    """
    INSERT OR IGNORE INTO historial_clinico(fecha,diagnostico,tratamiento,id_paciente)
    VALUES(?,?,?,?)
    """,
    ("22/07/2026","Alergia","Loratadina",3)
)

# PASO 5: Guardar todos los cambios realizados en la base de datos
conexion.commit()

# PASO 6: Consultar todos los registros de la tabla pacientes
cursor.execute("SELECT * FROM paciente")

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

# Crea la ventana principal del sistema.
ventana = Tk()

# Título de la ventana.
ventana.title("Sistema de Gestión de Citas Médicas")

# Tamaño de la ventana.
ventana.geometry("700x550")

# Evita que el usuario cambie el tamaño.
ventana.resizable(False, False)

# Color de fondo.
ventana.configure(bg="#EAF6FF")

# Título principal.
Label(
    ventana,
    text="SISTEMA DE GESTIÓN DE CITAS MÉDICAS",
    font=("Arial",18,"bold"),
    bg="#EAF6FF",
    fg="#0B4F6C"
).pack(pady=20)

# Subtítulo.
Label(
    ventana,
    text="Proyecto - Lenguaje de Programación II",
    font=("Arial",11),
    bg="#EAF6FF"
).pack()

# Línea informativa.
Label(
    ventana,
    text="Interfaz gráfica del sistema",
    font=("Arial",10),
    bg="#EAF6FF"
).pack(pady=10)

def registrar_paciente():  # Función que representa el registro de un paciente

    messagebox.showinfo(  # Muestra un mensaje informativo
        "Paciente",  # Título de la ventana
        "Función: Registrar Paciente"  # Mensaje mostrado al usuario
    )

def consultar_historial():  # Función que representa la consulta del historial clínico

    messagebox.showinfo(  # Muestra una ventana informativa
        "Paciente",  # Título
        "Función: Consultar Historial"  # Mensaje
    )

def registrar_medico():  # Función que representa el registro de un médico

    messagebox.showinfo(  # Muestra un mensaje informativo
        "Médico",  # Título
        "Función: Registrar Médico"  # Mensaje
    )

def consultar_agenda():  # Función que representa la consulta de la agenda médica

    messagebox.showinfo(  # Muestra una ventana informativa
        "Médico",  # Título
        "Función: Consultar Agenda"  # Mensaje
    )

def agendar_cita():  # Función que representa el agendamiento de una cita

    messagebox.showinfo(  # Muestra un mensaje informativo
        "Cita",  # Título
        "Función: Agendar Cita"  # Mensaje
    )

def cancelar_reprogramar():  # Función que representa cancelar o reprogramar una cita

    messagebox.showinfo(  # Muestra una ventana informativa
        "Cita",  # Título
        "Función: Cancelar o Reprogramar Cita"  # Mensaje
    )

def agregar_registro():  # Función que representa agregar un registro clínico

    messagebox.showinfo(  # Muestra un mensaje informativo
        "Historial Clínico",  # Título
        "Función: Agregar Registro Clínico"  # Mensaje
    )

def mostrar_historial():  # Función que representa mostrar el historial clínico

    messagebox.showinfo(  # Muestra una ventana informativa
        "Historial Clínico",  # Título
        "Función: Mostrar Historial"  # Mensaje
    )

# Crea un marco para organizar los botones
marco = Frame(
    ventana,  # La ventana principal será el contenedor padre
    bg="#EAF6FF"  # Color de fondo del contenedor
)

marco.pack(pady=20)  # Coloca el marco dentro de la ventana principal

# Botón que representa la opción Registrar Paciente
Button(
    marco,  # Se coloca dentro del marco
    text="Registrar Paciente",  # Texto mostrado al usuario
    width=30,  # Ancho del botón
    command=registrar_paciente  # Ejecuta la función registrar_paciente cuando se hace clic
).pack(pady=5)  # Coloca el botón en la ventana

Button(
    marco,
    text="Consultar Historial",
    width=30,
    command=consultar_historial
).pack(pady=5)

Button(
    marco,
    text="Registrar Médico",
    width=30,
    command=registrar_medico
).pack(pady=5)

Button(
    marco,
    text="Consultar Agenda",
    width=30,
    command=consultar_agenda
).pack(pady=5)

Button(
    marco,
    text="Agendar Cita",
    width=30,
    command=agendar_cita
).pack(pady=5)

Button(
    marco,
    text="Cancelar / Reprogramar Cita",
    width=30,
    command=cancelar_reprogramar
).pack(pady=5)

Button(
    marco,
    text="Agregar Registro Clínico",
    width=30,
    command=agregar_registro
).pack(pady=5)

Button(
    marco,
    text="Mostrar Historial",
    width=30,
    command=mostrar_historial
).pack(pady=5)

# Botón para cerrar la aplicación
Button(
    marco,  # Se coloca dentro del marco
    text="Salir",  # Texto mostrado
    width=30,  # Ancho
    bg="firebrick",  # Color de fondo
    fg="white",  # Color de la letra
    command=ventana.destroy  # Cierra completamente la aplicación
).pack(pady=10)  # Muestra el botón

# Mantiene abierta la ventana.
ventana.mainloop()
