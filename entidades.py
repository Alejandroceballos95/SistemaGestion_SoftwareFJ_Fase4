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
