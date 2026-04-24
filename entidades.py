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
# Aquí el compañero debe crear la clase abstracta Servicios y sus hijas
