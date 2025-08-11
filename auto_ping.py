import os

# Script de Python para automatizar una prueba de conectividad (ping)

# Dirección IP a la que haremos ping
ip_destino = "192.168.26.1"

print(f"Haciendo ping a {ip_destino} para comprobar la conectividad...")

# Ejecutar el comando ping
# '-c 4' en Linux hace 4 pings. En Windows, se usaría '-n 4'
response = os.system(f"ping -c 4 {ip_destino}")

# Analizar el resultado del comando
if response == 0:
    print(f"[+] ¡Éxito! {ip_destino} está activo y respondiendo.")
else:
    print(f"[-] Error: {ip_destino} no está respondiendo o el firewall lo está bloqueando.")