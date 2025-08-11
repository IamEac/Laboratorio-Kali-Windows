# Laboratorio de Hacking Ético: Análisis de Máquina Windows 11

## 📜 Resumen del Proyecto

Este repositorio documenta un laboratorio de hacking ético realizado en un entorno controlado con el fin de aprender el ciclo de vida de un ciberataque. El proyecto abarca desde el reconocimiento inicial hasta la obtención de persistencia, utilizando herramientas estándar de la industria.

## 🛠️ Herramientas y Tecnologías

- **Máquina Atacante:** Kali Linux (máquina virtual)
- **Máquina Objetivo:** Windows 11 (máquina virtual)
- **Plataforma:** VMware Workstation
- **Herramientas de Seguridad:**
    - **Nmap:** Escaneo de puertos y reconocimiento.
    - **Wireshark:** Análisis y detección de tráfico de red.
    - **Metasploit Framework:** Explotación y persistencia.
    - **Msfvenom:** Generación de payloads maliciosos.
    - **Python:** Scripting para automatización.

## 🗺️ Metodología del Ataque

El laboratorio siguió una metodología de ataque estándar para simular un escenario real:

1.  **Escaneo y Reconocimiento:** Se utilizó `Nmap` para identificar puertos abiertos en la máquina objetivo y determinar los servicios activos.



2.  **Detección de Tráfico:** Se analizó el tráfico con `Wireshark` para observar los paquetes del escaneo, demostrando que esta actividad de red es detectable.



3.  **Explotación Inicial:** A través de un ataque del lado del cliente, se ejecutó un payload malicioso para obtener una sesión `meterpreter` en la máquina Windows.

 

4.  **Persistencia:** Se instaló una puerta trasera (backdoor) para mantener el acceso al sistema, incluso después de un reinicio.

5.  **Análisis de Defensa:** Se validó la funcionalidad del firewall y antivirus de Windows, que lograron bloquear los intentos posteriores de conexión, demostrando la importancia de las defensas.

## 💡 Lecciones Aprendidas

- El ciclo completo de un ataque ético, desde la identificación de una vulnerabilidad hasta la obtención de acceso.
- La importancia de la persistencia y cómo se puede lograr en un sistema comprometido.
- El rol fundamental del firewall y el antivirus como defensas activas.
- La capacidad de automatizar tareas de hacking y defensa con scripting en Python.

## 📂 Archivos del Repositorio

- `auto_ping.py`: Script de Python para automatizar pruebas de conectividad.
- `reporte.md`: Reporte profesional de los hallazgos del laboratorio.
- `screenshots/`: Carpeta con capturas de pantalla de los puntos clave del proyecto.

---
