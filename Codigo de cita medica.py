'''Grupo: 2
Integrantes: Abarca Orrala Pedro Segundo, Delacruz Castillo Henry Alexander, 
Lopez Mendoza Genessis Milena, Piedra Ortega Francisco Andres, 
Quinde Eugenio Julexi Tatiana'''
# Librerías
import sqlite3  # Importa la librería sqlite3 para trabajar con bases de datos SQLite
from collections import deque  # Importa la estructura deque,que se utilizará como una cola (FIFO)
from tkinter import *  # Importa todos los componentes de Tkinter para crear la interfaz gráfica
from tkinter import messagebox  # Permite mostrar ventanas emergentes con mensajes informativos

# ===========================================
# CLASE DEL DOMINIO
# ===========================================
# Se crea la clase Persona para representar la información
# común que tendrán pacientes y médicos
class Persona:
    # Constructor de la clase Persona
    # Se ejecuta automáticamente cuando se crea un objeto
    def __init__(self, nombre, cedula,telefono):
        self.__nombre = nombre  # Guarda el nombre como un atributo privado
        self.__cedula = cedula  # Guarda la cédula como un atributo privado
        self.__telefono = telefono  # Guarda el telefono como un atributo privado
    def get_nombre(self):
        return self.__nombre  # Obtiene el nombre de la persona
    
    def get_cedula(self):
        return self.__cedula  # Obtiene la cédula de la persona

    def get_telefono(self):
        return self.__telefono  # Obtiene el teléfono de la persona
    
    # Actualiza el nombre de la persona
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Actualiza la cédula de la persona
    def set_cedula(self, cedula):
        self.__cedula = cedula

    # Actualiza el teléfono de la persona
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
        self.__edad = edad  # Guarda la edad del paciente

    # Obtiene el identificador del paciente
    def get_id_paciente(self):
        return self.__id_paciente
    
    # Obtiene la edad del paciente
    def get_edad(self):
        return self.__edad
    
    # Actualiza la edad del paciente
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

        # Llama al constructor de Persona
        super().__init__(nombre, cedula,telefono)

        # Guarda el identificador del médico
        self.__id_medico = id_medico

        # Guarda la especialidad médica
        self.__especialidad = especialidad

        # Guarda el consultorio asignado
        self.__consultorio = consultorio

    # Métodos Get y Devuelve el ID
    def get_id_medico(self):
        return self.__id_medico  # Obtiene el identificador del médico

    def get_especialidad(self):
        return self.__especialidad  # Obtiene la especialidad del médico

    def get_consultorio(self):
        return self.__consultorio  # Obtiene el consultorio del médico

    # Actualiza la especialidad del médico
    def set_especialidad(self, especialidad):
        self.__especialidad = especialidad

    # Actualiza el consultorio del médico
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

# La clase Cita representa la información correspondiente
# a una cita médica programada
class Cita:

    # Constructor de la clase Cita
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
        return self.__id_paciente  # Devuelve el identificador del paciente

    def get_id_medico(self):
        return self.__id_medico  # Devuelve el identificador del medico

    def set_fecha(self, fecha):
        self.__fecha = fecha  # Actualiza la fecha de la cita

    def set_hora(self, hora):
        self.__hora = hora  # Actualiza la hora de la cita

    def set_estado(self, estado):
        self.__estado = estado  # Actualiza el estado de la cita
# Representa el historial de un paciente
class HistorialClinico:

    # Constructor de la clase HistorialClinico
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

        # Guarda el paciente asociado
        self.__id_paciente = id_paciente  # Guarda el identificador de paciente
                     
    def get_id_historial(self):
        return self.__id_historial  # Devuelve el identificador del historial
    
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
        self.__fecha = fecha  # Actualiza la fecha del historial

    def set_diagnostico(self, diagnostico):
        self.__diagnostico = diagnostico  # Actualiza el diagnostico del historial

    def set_tratamiento(self, tratamiento):
        self.__tratamiento = tratamiento  # Actualiza el tratamiento del historial

# ===========================================
# ESTRUCTURA DE DATOS
# ===========================================

# Se crea una cola vacía para almacenar los pacientes en espera
cola_espera = deque()

cola_espera.append("Pedro Vera")  # Agrega un paciente al final de la cola
cola_espera.append("María López")  #Agrega otro paciente al final de la cola
cola_espera.append("Carlos Pizarro")  # Agrega un tercer paciente al final de la cola

# Función para atender al siguiente paciente de la cola
def atender_paciente():

    if len(cola_espera) > 0:  # Verifica si existen pacientes en espera
        return cola_espera.popleft()  # Elimina y devuelve el primer paciente

    return "No hay pacientes en espera"  # Si la cola está vacía devuelve un mensaje informativo

print("\n")
print("=" * 60)
print("        COLA (SALA DE ESPERA)")
print("=" * 60)

print("Pacientes en espera:")
print(list(cola_espera))  # Convierte la cola en una lista para visualizarla y con el print se visualiza

print("\nSe atiende al primer paciente:")

print(atender_paciente())

print("\nCola después de atender:")

print(list(cola_espera))

pila_historial = []

pila_historial.append("Gripe")  # Inserta el historial al final de la pila
pila_historial.append("Migraña")  # Inserta otro historial al final de la pila
pila_historial.append("Alergia")  # Agrega un tercer historial al final de la pila

# Devuelve el último historial registrado
def ultima_atencion():

    # Verifica si la pila tiene elementos
    if len(pila_historial) > 0:

        # Devuelve el último elemento
        return pila_historial[-1]

    # Si la pila está vacía
    return "No existen historiales"

# Elimina el último historial registrado
def eliminar_ultima_atencion():

    # Verifica si existen historiales
    if len(pila_historial) > 0:

        # Elimina el último elemento
        pila_historial.pop()

        return "Última atención eliminada"

    # Si la pila está vacía
    return "No existen historiales"

print("\n")
print("=" * 60)
print("        PILA (HISTORIAL CLÍNICO)")
print("=" * 60)

print("Historial almacenado:")

print(pila_historial)

print("\nÚltima atención registrada:")

print(ultima_atencion())

print("\nSe elimina la última atención")

eliminar_ultima_atencion()

print("\nHistorial actualizado")

print(pila_historial)

lista_citas = []

lista_citas.append("20/07/2026 08:00")  # Inserta la cita al final de la lista
lista_citas.append("21/07/2026 09:00")  # Inserta otra cita al final de la lista
lista_citas.append("22/07/2026 10:30")  # Agrega una tercera cita al final de la lista

print("\n")
print("=" * 60)
print("        LISTA DE CITAS")
print("=" * 60)

print("Citas registradas:")

print(lista_citas)

print("\nRecorrido de la lista:")

for cita in lista_citas:
    print(cita)

print("\n")
print("=" * 60)
print("        BÚSQUEDA SECUENCIAL")
print("=" * 60)

# Lista de pacientes utilizada para el ejemplo de búsqueda
pacientes = [
    "Pedro",
    "Maria",
    "Carlos"
]

# Muestra la lista completa
print("Lista de pacientes registrados:")

for paciente in pacientes:
    print("-", paciente)

# Paciente que se desea buscar
buscar = "Carlos"

print("\nPaciente a buscar:", buscar)

# Variable para verificar si fue encontrado
encontrado = False

# Recorre la lista uno por uno
for paciente in pacientes:

    # Compara el nombre buscado
    if paciente == buscar:

        print("\nPaciente encontrado correctamente")  # Muestra un mensaje cuando encuentra coincidencia
        print("Nombre:", paciente)

        encontrado = True

        break

# Si no existe en la lista
if encontrado == False:

    print("\nPaciente no encontrado.")
# ===========================================
# BASE DE DATOS
# ===========================================

# PASO 1: Conectar con la base de datos
conexion = sqlite3.connect("clinica.db")  # Si el archivo no existe,SQLite lo crea automáticamente

# PASO 2: Crear el cursor para ejecutar instrucciones SQL
cursor = conexion.cursor()

# PASO 3: Creacion de las tablas si todavía no existe
# -----------------------------------------------------
# TABLA PACIENTE
# -----------------------------------------------------
cursor.execute("""
    CREATE TABLE IF NOT EXISTS paciente(

        id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,

        nombre TEXT NOT NULL,

        cedula TEXT UNIQUE NOT NULL,

        edad INTEGER NOT NULL,

        telefono TEXT NOT NULL

    )

    """)
# -----------------------------------------------------
# TABLA MEDICO
# -----------------------------------------------------
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
# PASO 4: Insertar los datos de las tablas en la base de datos

# -----------------------------
# PACIENTES
# -----------------------------
# Registra tres pacientes de ejemplo
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
# Registra tres médicos de ejemplo
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
# Registra tres citas médicas de ejemplo
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
# Registra tres historiales clínicos de ejemplo
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

# Crea la ventana principal del sistema
ventana = Tk()

# Título de la ventana
ventana.title("Sistema de Gestión de Citas Médicas")

# Tamaño de la ventana
ventana.geometry("700x550")

# Evita que el usuario cambie el tamaño
ventana.resizable(False, False)

# Color de fondo
ventana.configure(bg="#EAF6FF")

# Muestra el título principal del sistema
Label(
    ventana,
    text="SISTEMA DE GESTIÓN DE CITAS MÉDICAS",
    font=("Arial",18,"bold"),
    bg="#EAF6FF",
    fg="#0B4F6C"
).pack(pady=20)

# Subtitulo
Label(
    ventana,
    text="Proyecto - Lenguaje de Programación II",
    font=("Arial",11),
    bg="#EAF6FF"
).pack()

# Muestra una breve descripción de la interfaz
Label(
    ventana,
    text="Interfaz gráfica del sistema",
    font=("Arial",10),
    bg="#EAF6FF"
).pack(pady=10)

def registrar_paciente():  # Función que permite registrar un paciente en la base de datos

    def guardar_paciente():
        nombre = entrada_nombre.get().strip()  # Obtiene el valor del campo de entrada y elimina espacios en blanco al inicio y al final
        cedula = entrada_cedula.get().strip()  # Obtiene el valor del campo de entrada y elimina espacios en blanco al inicio y al final
        edad = entrada_edad.get().strip()  # Obtiene el valor del campo de entrada y elimina espacios en blanco al inicio y al final
        telefono = entrada_telefono.get().strip()  # Obtiene el valor del campo de entrada y elimina espacios en blanco al inicio y al final

        if not nombre or not cedula or not edad or not telefono:  # Verifica que ningún campo quede vacío
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:  # Comprueba que la edad sea un número entero
            edad_int = int(edad)
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número entero.")
            return

        try:  # Intenta registrar el paciente en la base de datos
            conexion_registro = sqlite3.connect("clinica.db")
            cursor_registro = conexion_registro.cursor()
            cursor_registro.execute(  # Ejecuta la consulta SQL para guardar el paciente
                "INSERT INTO paciente(nombre, cedula, edad, telefono) VALUES (?, ?, ?, ?)",
                (nombre, cedula, edad_int, telefono)
            )
            conexion_registro.commit()  # Guarda permanentemente los cambios realizados
            conexion_registro.close()  # Cierra la conexión con la base de datos

            messagebox.showinfo("Éxito", "Paciente registrado correctamente")  # Informa que el registro fue exitoso
            ventana_registro.destroy()  # Cierra la ventana de registro
        except sqlite3.IntegrityError:  # Se ejecuta si la cédula ya existe
            messagebox.showerror("Error", "La cédula ya está registrada.")
        except Exception as e:  # Captura cualquier otro error inesperado
            messagebox.showerror("Error", f"No se pudo registrar el paciente.\n{e}")

    ventana_registro = Toplevel(ventana)  # Crea una ventana secundaria para registrar pacientes
    ventana_registro.title("Registrar Paciente")  # Asigna el título de la ventana
    ventana_registro.geometry("400x300")  # Define el tamaño de la ventana
    ventana_registro.resizable(False, False)  # Impide modificar el tamaño
    ventana_registro.configure(bg="#EAF6FF")  # Cambia el color de fondo

    Label(ventana_registro, text="Registrar Paciente", font=("Arial", 14, "bold"), bg="#EAF6FF").pack(pady=10)

    frame_campos = Frame(ventana_registro, bg="#EAF6FF")  # Cambia el color de fondo
    frame_campos.pack(padx=20, pady=10, fill="x")

    Label(frame_campos, text="Nombre:", bg="#EAF6FF").grid(row=0, column=0, sticky="w", pady=5)  # Etiqueta para ingresar el nombre
    entrada_nombre = Entry(frame_campos, width=30)  # Caja de texto donde se escribe el nombre
    entrada_nombre.grid(row=0, column=1, pady=5)

    Label(frame_campos, text="Cédula:", bg="#EAF6FF").grid(row=1, column=0, sticky="w", pady=5)
    entrada_cedula = Entry(frame_campos, width=30)
    entrada_cedula.grid(row=1, column=1, pady=5)

    Label(frame_campos, text="Edad:", bg="#EAF6FF").grid(row=2, column=0, sticky="w", pady=5)
    entrada_edad = Entry(frame_campos, width=30)
    entrada_edad.grid(row=2, column=1, pady=5)

    Label(frame_campos, text="Teléfono:", bg="#EAF6FF").grid(row=3, column=0, sticky="w", pady=5)
    entrada_telefono = Entry(frame_campos, width=30)
    entrada_telefono.grid(row=3, column=1, pady=5)

    Button(ventana_registro, text="Guardar", width=20, command=guardar_paciente).pack(pady=15)  # Botón que guarda la información del paciente

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

Button(  # Botón para consultar el historial clínico
    marco,
    text="Consultar Historial",
    width=30,
    command=consultar_historial
).pack(pady=5)

Button(  # Botón para registrar un médico
    marco,
    text="Registrar Médico",
    width=30,
    command=registrar_medico
).pack(pady=5)

Button(  # Botón para consultar la agenda médica
    marco,
    text="Consultar Agenda",
    width=30,
    command=consultar_agenda
).pack(pady=5)

Button(  # Botón para agendar una cita
    marco,
    text="Agendar Cita",
    width=30,
    command=agendar_cita
).pack(pady=5)

Button(  # Botón para cancelar o reprogramar una cita
    marco,
    text="Cancelar / Reprogramar Cita",
    width=30,
    command=cancelar_reprogramar
).pack(pady=5)

Button(  # Botón para agregar un registro clínico
    marco,
    text="Agregar Registro Clínico",
    width=30,
    command=agregar_registro
).pack(pady=5)

Button(  # Botón para mostrar el historial clínico
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

# Mantiene abierta la ventana
ventana.mainloop()
