# Usar la imagen oficial de Node.js como imagen base
FROM node:20

COPY init_script.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/init_script.sh

# Establecer el script de inicialización como entrada por defecto
ENTRYPOINT ["/usr/local/bin/init_script.sh"]


# Crear y definir el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el package.json y package-lock.json al directorio de trabajo
COPY package*.json ./

# Instalar las dependencias del proyecto
RUN npm install -g @ionic/cli
RUN npm install -g @angular/cli
RUN npm install

# Copiar todos los archivos del proyecto al directorio de trabajo
COPY . .

# Exponer el puerto 8100 (puerto por defecto de ionic serve)
EXPOSE 8100

# Comando por defecto para correr la aplicación
CMD ["ionic", "serve", "--host", "0.0.0.0", "--port", "8100"]
