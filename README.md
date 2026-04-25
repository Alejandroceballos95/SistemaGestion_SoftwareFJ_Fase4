# 🚀 Sistema Integral de Gestión - Software FJ (Fase 4)

Bienvenidos al repositorio del **Sistema de Gestión de Clientes, Servicios y Reservas** para la empresa *Software FJ*. Este proyecto ha sido desarrollado como parte de la Fase 4 del curso de Programación (213023).

## 📋 Descripción del Proyecto
Software FJ es una empresa que ofrece servicios de **reserva de salas, alquiler de equipos y asesorías especializadas**. 

El objetivo de esta aplicación es simular el flujo operativo de la empresa (recepción, validación y registro) aplicando los pilares de la **Programación Orientada a Objetos (POO)** y un manejo robusto de **Excepciones**, garantizando que el sistema nunca se detenga ante datos inválidos.

> ⚠️ **Nota Importante:** Este sistema opera íntegramente en memoria (Listas de Python) y archivos de texto plano (.log). No utiliza motores de bases de datos externos.

---

## 🏗️ Arquitectura del Sistema: ¿Cómo funciona?

Para entender el código, imagina que el sistema es un edificio físico de oficinas:

| Archivo | Rol en el "Negocio" | Concepto de Programación |
| :--- | :--- | :--- |
| **`entidades.py`** | **Los Formularios:** Define los requisitos para registrar un Cliente o un Servicio. | Abstracción, Herencia, Encapsulación y Polimorfismo. |
| **`reservas.py`** | **La Recepcionista:** Toma un Cliente y un Servicio para crear un ticket de reserva. | Composición de Objetos. |
| **`excepciones.py`** | **El Guarda de Seguridad:** Detiene procesos con datos malos pero deja que el negocio siga abierto. | Excepciones Personalizadas. |
| **`logger.py`** | **La Bitácora del Gerente:** Anota cada incidente o error ocurrido durante el día en `errores.log`. | Manejo de archivos (I/O). |
| **`main.py`** | **El Administrador:** Es quien abre el negocio y ejecuta la simulación de 10 operaciones. | Flujo de control y Lógica Principal. |

---

## 🛠️ Plan de Trabajo y Roles

Para mantener el orden y evitar conflictos en el código, el equipo se ha dividido en los siguientes módulos:

1.  **Arquitectura Base:** Creación de clases abstractas y estructura de archivos (Responsable: Alejandro).
2.  **Módulo de Clientes:** Implementación de la clase `Cliente` con validaciones y encapsulamiento.
3.  **Módulo de Servicios:** Implementación de herencia y polimorfismo en tipos de servicios.
4.  **Gestión de Reservas:** Lógica de confirmación, cancelación e integración de objetos.
5.  **QA y Excepciones:** Programación de la simulación de 10 operaciones y manejo de errores.

---

## 💻 Instrucciones para Desarrolladores (Equipo)

### 1. Uso de Ramas (Branches)
**¡No trabajes directamente en la rama `main`!** Sigue este flujo:
1. Crea tu propia rama: `git checkout -b nombre-de-tu-modulo`
2. Realiza tus cambios y haz commit.
3. Sube tu rama: `git push origin nombre-de-tu-modulo`
4. Avisa al Arquitecto Base para realizar la integración (Merge).

### 2. Regla de Oro
Todo proceso crítico debe estar envuelto en bloques `try...except`. Si ocurre un error, debe reportarse al `logger` y el programa debe continuar con la siguiente operación.

---
*Desarrollado para el curso de Programación - UNAD 2026*