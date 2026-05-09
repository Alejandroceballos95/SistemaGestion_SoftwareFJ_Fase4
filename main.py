import entidades
import reservas
import excepciones
from logger import Logger


def mostrar_menu():
    print("\n" + "="*45)
    print("SISTEMA DE GESTIÓN - SOFTWARE FJ")
    print("="*45)
    print("1. Registrar un nuevo Cliente")
    print("2. Crear un nuevo Servicio")
    print("3. Generar una Reserva")
    print("4. Confirmar una Reserva")
    print("5. Cancelar una Reserva")
    print("6. Ver todos los registros (Reporte)")
    print("7. Salir del sistema")
    print("="*45)


def main():
    # Listas en memoria
    lista_clientes = []
    lista_servicios = []
    lista_reservas = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            # OPCIÓN 1: Registrar Cliente
            print("\n--- REGISTRO DE CLIENTE ---")
            identificacion = input("Ingrese el ID (sólo números): ")
            nombre = input("Ingrese el nombre (sólo letras): ")
            email = input("Ingrese el email: ")
            telefono = input("Ingrese el teléfono (mín. 7 números): ")

            try:
                nuevo_cliente = entidades.Cliente(
                    identificacion, nombre, email, telefono)
                lista_clientes.append(nuevo_cliente)
                print(f"¡Éxito! Cliente {nombre} registrado correctamente.")
            except excepciones.SistemaGestionError as e:
                print(f"ERROR: {e}")
                print("El programa no se cerrará. Revisa 'errores.log'.")
                Logger.registrar_error(f"Fallo al crear cliente: {e}")

        elif opcion == "2":
            # OPCIÓN 2: Crear Servicio
            print("\n--- CREACIÓN DE SERVICIO ---")
            print("Tipos: 1. Asesoría | 2. Alquiler de Equipo | 3. Reserva de Sala")
            tipo = input("Seleccione el tipo de servicio (1/2/3): ")

            codigo = input("Ingrese el código del servicio (Ej. S01): ")
            descripcion = input("Ingrese la descripción: ")

            try:
                precio_base = float(input("Ingrese el precio base (número): "))

                if tipo == "1":
                    servicio = entidades.Asesoria(
                        codigo, descripcion, precio_base)
                elif tipo == "2":
                    servicio = entidades.AlquilerEquipo(
                        codigo, descripcion, precio_base)
                elif tipo == "3":
                    servicio = entidades.ReservaSala(
                        codigo, descripcion, precio_base)
                else:
                    print("Opción de tipo de servicio no válida.")
                    continue

                lista_servicios.append(servicio)
                print(
                    f"¡Éxito! Servicio '{descripcion}' creado correctamente.")

            except ValueError:
                print("ERROR: El precio base debe ser un valor numérico.")
                Logger.registrar_error(
                    "Fallo al crear servicio: El precio base no es un número.")
            except excepciones.SistemaGestionError as e:
                print(f"ERROR: {e}")
                Logger.registrar_error(f"Fallo al crear servicio: {e}")

        elif opcion == "3":
            # OPCIÓN 3: Generar Reserva
            print("\n--- GENERAR RESERVA ---")
            if not lista_clientes or not lista_servicios:
                print("Debes tener al menos un cliente y un servicio registrados.")
                continue

            # Mostrar clientes
            print("Clientes disponibles:")
            for i, c in enumerate(lista_clientes):
                print(f"  {i}. {c._nombre} (ID: {c._identificacion})")

            # Mostrar servicios
            print("\nServicios disponibles:")
            for i, s in enumerate(lista_servicios):
                print(f"  {i}. {s._descripcion} - Base: ${s._precio_base}")

            try:
                idx_cliente = int(
                    input("\nSeleccione el número del cliente: "))
                idx_servicio = int(
                    input("Seleccione el número del servicio: "))
                tiempo = float(
                    input("Ingrese la cantidad de tiempo (horas o días según aplique): "))

                cliente_sel = lista_clientes[idx_cliente]
                servicio_sel = lista_servicios[idx_servicio]

                nueva_reserva = reservas.Reserva(
                    cliente_sel, servicio_sel, tiempo)
                lista_reservas.append(nueva_reserva)
                print("¡Éxito! Reserva generada:")
                print("   ->", nueva_reserva.mostrar_resumen())

            except (ValueError, IndexError):
                print(
                    "ERROR: Selección inválida. Debes ingresar el número correcto de la lista.")
                Logger.registrar_error(
                    "Fallo en reserva: Selección de índices inválida en listas.")
            except excepciones.SistemaGestionError as e:
                print(f"ERROR: {e}")
                Logger.registrar_error(f"Fallo al reservar: {e}")

        elif opcion == "4":
            # OPCIÓN 4: Confirmar Reserva
            print("\n--- CONFIRMAR RESERVA ---")
            if not lista_reservas:
                print("No hay reservas creadas.")
                continue

            for i, r in enumerate(lista_reservas):
                print(f"  {i}. {r.mostrar_resumen()}")

            try:
                idx = int(
                    input("\nSeleccione el número de la reserva a confirmar: "))
                lista_reservas[idx].confirmar()
                print(
                    f"Reserva de {lista_reservas[idx].cliente._nombre} confirmada con éxito.")
            except (ValueError, IndexError):
                print("ERROR: Selección inválida.")
            except excepciones.SistemaGestionError as e:
                print(f"ERROR: {e}")
                Logger.registrar_error(f"Fallo al confirmar: {e}")

        elif opcion == "5":
            # OPCIÓN 5: Cancelar Reserva
            print("\n--- CANCELAR RESERVA ---")
            if not lista_reservas:
                print("No hay reservas creadas.")
                continue

            for i, r in enumerate(lista_reservas):
                print(f"  {i}. {r.mostrar_resumen()}")

            try:
                idx = int(
                    input("\nSeleccione el número de la reserva a cancelar: "))
                lista_reservas[idx].cancelar()
                print(
                    f"Reserva de {lista_reservas[idx].cliente._nombre} cancelada con éxito.")
            except (ValueError, IndexError):
                print("ERROR: Selección inválida.")
            except excepciones.SistemaGestionError as e:
                print(f"ERROR: {e}")
                Logger.registrar_error(f"Fallo al cancelar: {e}")

        elif opcion == "6":
            # OPCIÓN 6: Ver Reportes
            print("\n--- REPORTES DEL SISTEMA ---")
            print(f"Total Clientes: {len(lista_clientes)}")
            print(f"Total Servicios: {len(lista_servicios)}")
            print(f"Total Reservas: {len(lista_reservas)}\n")
            for r in lista_reservas:
                print(f"- {r.mostrar_resumen()}")

        elif opcion == "7":
            # OPCIÓN 7: Salir
            print("\nSaliendo del sistema Software FJ... ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
