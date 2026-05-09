# 🚀 Sistema Integral de Gestión - Software FJ

Bienvenido al **Sistema de Gestión de Clientes, Servicios y Reservas** de la empresa *Software FJ*. Este proyecto es una solución de consola basada íntegramente en los pilares de la Programación Orientada a Objetos (POO) desarrollada para la Fase 4 del curso de Programación.

## 📋 Descripción del Software

El sistema simula el flujo operativo de una empresa que ofrece:
1. **Asesorías especializadas.**
2. **Alquiler de equipos tecnológicos.**
3. **Reserva de salas físicas.**

La característica principal de este software es su **arquitectura a prueba de fallos**. A través de un manejo avanzado de excepciones personalizadas, el sistema es capaz de detectar datos inválidos o acciones ilógicas sin detener su ejecución, registrando cualquier anomalía en una bitácora física.

---

## ⚙️ ¿Cómo ejecutar el programa?

Para iniciar la simulación del sistema, asegúrate de tener Python instalado en tu equipo y ejecuta el archivo principal desde tu terminal:

python main.py

### ¿Qué sucederá al ejecutarlo?
El sistema ejecutará automáticamente una prueba de control de calidad (QA) que consta de **10 operaciones secuenciales**. 
Verás en tu consola cómo el programa registra clientes y servicios válidos, crea y cancela reservas, y cómo **atrapa intencionalmente** operaciones inválidas (como correos mal escritos o intentos de cancelar una reserva que ya estaba cancelada).

---

## 📂 Estructura del Proyecto

El sistema está construido de forma modular para garantizar su escalabilidad:

* **`main.py`**: Archivo principal que orquesta la ejecución y realiza la simulación de las 10 operaciones.
* **`entidades.py`**: Contiene las clases abstractas y concretas de los `Clientes` y `Servicios`, aplicando herencia y polimorfismo para el cálculo de costos.
* **`reservas.py`**: Implementa el concepto de composición, uniendo a un Cliente con un Servicio para gestionar el ciclo de vida de un ticket de reserva.
* **`excepciones.py`**: Define los errores personalizados (`DatoInvalidoError`, `OperacionNoPermitidaError`, etc.) para controlar el flujo del negocio.
* **`logger.py`**: Utilidad encargada de crear y escribir en el archivo `errores.log`.

---

## 📝 Registro de Errores (Logs)

Si durante la ejecución se detecta una operación inválida, el sistema informará en pantalla pero **no se cerrará**. En su lugar, el incidente quedará guardado con su fecha y hora exacta en un archivo de texto llamado:

📄 `errores.log` *(Este archivo se generará automáticamente en la raíz del proyecto tras la primera ejecución).*

---
*Desarrollado como proyecto académico para la Universidad Nacional Abierta y a Distancia (UNAD).*