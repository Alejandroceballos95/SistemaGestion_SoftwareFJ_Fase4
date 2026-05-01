class SistemaGestionError(Exception):
    """
    Clase base fundamental para nuestro sistema.
    Todas las demás excepciones heredarán de este lugar de la genérica de Python.
    """


class DatoInvalidoError(SistemaGestionError):
    """
    Lanzada cuando un dato ingresado (como el ID del cliente) no cumpleel formato.
    """

    def __init__(self, mensaje="Error de validación: El dato ingresado es incorrecto."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class RecursoNoDisponibleError(SistemaGestionError):
    """
    Lanzada cuando se intenta hacer una acción ilógica (ej: cancelar una reserva ya cancelada).
    """

    def __init__(self, mensaje="Error de operación: Acción no permitida en este estado."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
