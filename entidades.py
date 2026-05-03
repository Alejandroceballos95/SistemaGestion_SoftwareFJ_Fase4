import re
from abc import ABC, abstractmethod
# Importamos las excepciones personalizadas
from excepciones import DatoInvalidoError

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

"""Clase cliente que hereda los atributos de la clase general"""


class Cliente(EntidadGeneral):  # Aplicamos la herencia
    def __init__(self, identificacion, nombre, email, telefono):
        # Llamamos al constructor de la clase padre
        super().__init__(identificacion, nombre)
        # Ejecutamos las validaciones aplicadas por Jorge
        self._validar_identificacion(identificacion)
        self._validar_nombre(nombre)
        self.set_email(email)
        self.set_telefono(telefono)

    # Validaciones de Jorge adaptadas a las excepciones

    def _validar_identificacion(self, identificacion):
        if not str(identificacion).isdigit():
            raise DatoInvalidoError("El ID debe contener sólo números ")

    def _validar_nombre(self, nombre):
        if not nombre or not nombre.replace(" ", "").isalpha():
            raise DatoInvalidoError(
                "El nombre no debe estar vacío y sólo debe contener letras")

    def set_email(self, email):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(patron, email):
            raise DatoInvalidoError("El email no tiene un formato válido")
        self.__email = email

    def set_telefono(self, telefono):
        if not str(telefono).isdigit() or len(str(telefono)) < 7:
            raise DatoInvalidoError(
                "El teléfono debe contener sólo números y tener al menos 7 dígitos")
        self.__telefono = telefono

    # GETTERS

    def get_email(self):
        return self.__email

    def get_telefono(self):
        return self.__telefono

    # Método obligatorio de la clase padre

    def mostrar_detalles(self):
        """Cumple con el polimorfismo exigido por EntidadGeneral"""
        return f"Cliente(ID: {self._identificacion}, Nombre: {self._nombre}, Email: {self.__email}, Teléfono: {self.__telefono})"

# ESPACIO PARA LA OPCIÓN 2 (Especialista en servicios)


class Servicio(ABC):
    """
    Clase abstracta que define la estructura básica de cualquier servicio ofrecido por Software FJ.
    """

    def __init__(self, codigo, descripcion, precio_base):
        self._codigo = codigo
        self._descripcion = descripcion
        self._precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, cantidad_tiempo):
        """Método polifórmico que cada servicio hijo calculará a su manera"""
        pass

    def mostrar_detalles(self):
        return f"[{self._codigo}] {self._descripcion} - Precio Base: ${self._precio_base}"


class Asesoria(Servicio):
    """Servicio que se cobra por horas de consultoría."""

    def calcular_costo(self, horas):
        # La asesoría cobra el precio base multiplicado por las horas
        return self._precio_base * horas


class AlquilerEquipo(Servicio):
    """Servicios que se cobra por días de alquiler."""

    def calcular_costo(self, dias):
        # El alquiler suma un 10% adicional por seguros de daños
        costo_total = self._precio_base * dias
        return costo_total + (costo_total * 0.10)
