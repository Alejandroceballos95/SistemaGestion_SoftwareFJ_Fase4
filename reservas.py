from excepciones import OperacionNoPermitidaError


class Reserva:
    """Clase que integra un cliente y un servicio para generar un ticket de reserva."""

    def __init__(self, cliente, servicio, cantidad_tiempo):
        self.cliente = cliente
        self.servicio = servicio
        self.cantidad_tiempo = cantidad_tiempo
        # Al nacer, toda reserva estará activada por defecto
        self.estado = "Activa"
        # Aquí aplicamos el poliformismo calculando el costo sin importar qué servicio sea
        self.costo_total = self.servicio.calcular_costo(cantidad_tiempo)

    def cancelar(self):
        if self.estado == "Cancelada":
            # Usamos la excepción personalizada para detener acciones ilógicas
            raise OperacionNoPermitidaError(
                "La reserva ya se encuentra cancelada y no se puede volver a cancelar.")
        self.estado = "Cancelada"

    def confirmar(self):
        if self.estado == "Cancelada":
            raise OperacionNoPermitidaError(
                "No se puede confirmar una reserva que ha sido cancelada.")
        self.estado = "Confirmada"

    def mostrar_resumen(self):
        return f"Reserva de {self.cliente._nombre} | Servicio: {self.servicio._descripcion} | Estado: {self.estado} | Total: {self.costo_total}"
