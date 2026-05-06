import datetime


class Logger:
    """
    Clase utilitaria encargada de registrar los eventos y errores del sistema en un archivo de texto físico.
    """

    @staticmethod
    def registrar_error(mensaje):
        # 1. Capturamos la fecha y hora exacta del sistema
        fecha_hora_actual = datetime.datetime.now()
        fecha_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")

        # 2. Armamos el mensaje final que se escribirá en el archivo
        log_mensaje = f"[{fecha_formateada}] ERROR: {mensaje}\n"

        # 3. Abrimos el archivo, escribimos el mensaje y lo cerramos automáticamente
        with open("errores.log", "a", encoding="utf-8") as archivo:
            archivo.write(log_mensaje)
