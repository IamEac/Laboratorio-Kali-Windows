# Laboratorio de Hacking Ético: Simulación de Ataque a Windows 11

## Objetivo
El objetivo de este laboratorio fue simular un ciclo completo de ataque ético, desde el reconocimiento hasta la obtención de persistencia, en un entorno de laboratorio controlado.

## Herramientas Utilizadas
- **Kali Linux** (como máquina atacante)
- **Windows 11** (como máquina objetivo)
- **VMware Workstation**
- **Nmap** (para escaneo de puertos)
- **Wireshark** (para análisis de tráfico)
- **Metasploit Framework** (para explotación y persistencia)

## Resumen del Proceso
1.  **Escaneo de Puertos:** Utilicé Nmap para escanear la máquina Windows, identificando puertos abiertos como 135, 139 y 445 (SMB).
2.  **Detección de Tráfico:** Analicé el tráfico en Wireshark para visualizar los paquetes del escaneo, demostrando que los ataques de red no son invisibles.
3.  **Explotación:** Usé un payload de Metasploit (a través de un ataque del lado del cliente) para obtener una sesión Meterpreter en la máquina Windows.
4.  **Persistencia:** Instalé una puerta trasera (backdoor) en Windows para mantener el acceso incluso después de reiniciar el sistema.
5.  **Defensa:** Demostré cómo el firewall y el antivirus de Windows bloquearon el intento de una nueva conexión, validando la importancia de las defensas.

## Habilidades Demostradas
- Comprensión de la metodología de un ataque.
- Uso de herramientas de hacking ético.
- Análisis de tráfico de red.
- Configuración de entornos de laboratorio.
- Entendimiento de la persistencia y la defensa.
