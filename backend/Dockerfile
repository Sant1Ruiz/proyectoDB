# Usar la imagen base oficial de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar las dependencias del sistema necesarias para psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de requisitos al directorio de trabajo
COPY requirements.txt .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación al directorio de trabajo
COPY . .

# Establecer las variables de entorno
ENV DB_HOST=host
ENV DB_DATABASE=db
ENV DB_USER=user
ENV DB_PASSWORD=pass

# Exponer el puerto en el que correrá la aplicación Flask
EXPOSE 80

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
