#!/bin/bash
apt update
apt install iputils-ping -y
# Realizar ping a backend y extraer la primera IP encontrada
BACKEND_IP=$(ping -c 1 backend | grep -oP '(\d+\.){3}\d+' | head -n 1)

# Exportar la IP obtenida como variable de entorno
export BACKEND_IP

# Mostrar la IP obtenida para propósitos de depuración
echo "La dirección IP del backend es: $BACKEND_IP"

echo "export const environment = { baseUrl: \"http://$BACKEND_IP:80\", production: false }; " > /app/src/environments/environment.ts

# Ejecutar el comando principal del contenedor
exec "$@"
