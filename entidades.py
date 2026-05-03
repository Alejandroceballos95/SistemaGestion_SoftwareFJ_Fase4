from abc import ABC, abstractmethod

# ESTA PARTE ES RESPONSABILIDAD DE ALEJANDRO CEBALLOS (Arquitecto Base)


class EntidadGeneral(ABC):
    """
    Clase abstracta principal que representa cualquier entidad del sistema (Clientes, Empleados, etc.).
    """

    def __init__(self, identificacion, nombre):
        self._identificacion = identificacion  # Atributo protegido
        self._nombre = nombre  # Atributo protegido

    @abstractmethod
    def mostrar_detalles(self):
        """Método abstracto que obliga a los hijos a implementarlo"""


# ESPACIO PARA LA OPCIÓN 1 (Especialista en clientes)
# Aquí el compañero debe crear la clase Cliente que herede de EntidadGeneral

"""primeramente hay que implementar la libreria "re" para validar textos con ciertos patrones
o simbolos asi como los correos electronicos y las contraseñas"""
import re
#creamos la clase cliente
class Cliente:
    #ahora comenzamos a hacer el constructor de la clase 
    def __init__(self, id_cliente, nombre, email, telefono):
        """iniciamos los atributos usando setter para aplicar validaciones
        para 
        """
        self.set_id_cliente(id_cliente)
        self.set_nombre(nombre)
        self.set_email(email)
        self.set_telefono(telefono)

    # =======================
    # GETTERS
    # =======================
    def get_id_cliente(self):
        return self.__id_cliente

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    def get_telefono(self):
        return self.__telefono

    # =======================
    # SETTERS CON VALIDACIÓN
    # =======================

    def set_id_cliente(self, id_cliente):
        """
        Valida que el ID solo contenga números.
        """
        if not str(id_cliente).isdigit():
            raise ValueError("El ID del cliente debe contener solo números.")
        self.__id_cliente = id_cliente

    def set_nombre(self, nombre):
        """
        Valida que el nombre no esté vacío y solo contenga letras.
        """
        if not nombre or not nombre.replace(" ", "").isalpha():
            raise ValueError("El nombre solo debe contener letras y no estar vacío.")
        self.__nombre = nombre

    def set_email(self, email):
        """
        Valida formato básico de email.
        """
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(patron, email):
            raise ValueError("El email no tiene un formato válido.")
        self.__email = email

    def set_telefono(self, telefono):
        """
        Valida que el teléfono tenga solo números y una longitud razonable.
        """
        if not str(telefono).isdigit() or len(str(telefono)) < 7:
            raise ValueError("El teléfono debe contener solo números y tener al menos 7 dígitos.")
        self.__telefono = telefono

    # =======================
    # MÉTODO ESPECIAL
    # =======================
    def __str__(self):
        """
        Representación en texto del cliente.
        """
        return f"Cliente(ID: {self.__id_cliente}, Nombre: {self.__nombre}, Email: {self.__email}, Teléfono: {self.__telefono})"


# ESPACIO PARA LA OPCIÓN 2 (Especialista en servicios)
# Aquí el compañero debe crear la clase abstracta Servicios y sus hijas
