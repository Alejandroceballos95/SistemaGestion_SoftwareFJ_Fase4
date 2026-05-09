import entidades
import reservas
import excepciones
from logger import Logger


def main():
    print("--- INICIANDO EL SISTEMA DE SOFTWARE FJ ---\n")

    # Listas en memoria
    Lista_clientes = []
    Lista_servicios = []
    Lista_reservas = []

    # SIMULACION DE 10 OPERACIONES (PRUEBA QA)

    # 1) Crear cliente válido
    try:
        print("Op1: Registrando cliente válido...")
        cliente1 = entidades.Cliente(
            "1001", "Alejandro Ceballos", "alejandroceballos@correo.com", "3101234567")
        Lista_clientes.append(cliente1)
        print("-> OK: Cliente registrado:", cliente1._nombre)
    except excepciones.SistemaGestionError as e:
        Logger.registrar_error(str(e))

    # 2) Crear cliente con ID inválido (Fallo intencional)
    try:
        print("\nOp 2: Registrando cliente con ID inválido (letras)...")
        cliente_malo = entidades.Cliente(
            "ABC", "Jorge Mertínez", "jorge@correo.com", "32012344567")
        Lista_clientes.append(cliente_malo)
    except excepciones.SistemaGestionError as e:
        print(f"-> ERROR CAPTURADO (Ver errores.log): {e}")
        Logger.registrar_error(f"Op 2: {str(e)}")

    # 3) Crear servicio de asesoría
    try:
        print("\nOp 3: Creando servicio de asesoría...")
        serv1 = entidades.Asesoria(
            "S01", "Asesoría en arquitectura de software", 50000)
        Lista_servicios.append(serv1)
        print("-> OK: Servicio creado:", serv1._descripcion)
    except excepciones.SistemaGestionError as e:
        Logger.registrar_error(str(e))

    # 4) Crear servicio de alquiler de equipo
    try:
        print("\nOp 4: Creando servicio de alquiler de equipos...")
        serv2 = entidades.AlquilerEquipo(
            "S02", "Alquiler de servidor AWS", 150000)
        Lista_servicios.append(serv2)
        print("-> OK: Servicio creado:", serv2._descripcion)
    except excepciones.SistemaGestionError as e:
        Logger.registrar_error(str(e))

    # 5) Crear servicio de reserva de sala
    try:
        print("\nOp 5: Creando servicio de reserva de sala...")
        serv3 = entidades.ReservaSala("S03", "Sala de juntas VIP", 80000)
        Lista_servicios.append(serv3)
        print("-> OK: Servicio creado:", serv3._descripcion)
    except excepciones.SistemaGestionError as e:
        Logger.registrar_error(str(e))

    # 6) Crear una reserva válida
    try:
        print("\nOp 6: Generando reserva para Alejandro...")
        reserva1 = reservas.Reserva(
            Lista_clientes[0], Lista_servicios[2], 4)  # 4 horas de sala VIP
        Lista_reservas.append(reserva1)
        print("-> OK:", reserva1.mostrar_resumen())
    except excepciones.SistemaGestionError as e:
        Logger.registrar_error(str(e))

    # 7) Confirmar la reserva
    try:
        print("\nOp 7: Confirmando la reserva anterior...")
        Lista_reservas[0].confirmar()
        print("-> OK: Estado actual ->", Lista_reservas[0].estado)
    except excepciones.SistemaGestionError as e:
        Logger.registrar_error(str(e))

    # 8) Cancelar la reserva
    try:
        print("\nOp 8: Cancelando la reserva...")
        Lista_reservas[0].cancelar()
        print("-> OK: Estado actual ->", Lista_reservas[0].estado)
    except excepciones.SistemaGestionError as e:
        Logger.registrar_error(str(e))

    # 9) Intentar cancelar la reserva ya cancelada (Fallo intencional)
    try:
        print("\nOp 9: Intentanco cancelar una reserva que ya está cancelada...")
        Lista_reservas[0].cancelar()
    except excepciones.SistemaGestionError as e:
        print(f"-> ERROR CAPTURADO (Ver errores.log): {e}")
        Logger.registrar_error(f"Op 9: {str(e)}")

    # 10) Crear cliente con email inválido (Fallo intencional)
    try:
        print("\nOp 10: Registrando cliente con email inválido...")
        cliente_malo2 = entidades.Cliente(
            "1002", "Salomé Londoño", "correo-sin-arroba.com", "3001234567")
        Lista_clientes.append(cliente_malo2)
    except excepciones.SistemaGestionError as e:
        print(f"-> ERROR CAPTURADO (Ver errores.log): {e}")
        Logger.registrar_error(f"Op 10: {str(e)}")

    print("\n--- SIMULACIÓN FINALIZADA ---")
    print("Si ves esto, el programa NO colapsó. Revisa 'errores.log' para ver el reporte de los fallos.")


if __name__ == "__main__":
    main()
