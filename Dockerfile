# Utilizar una imagen base de Python
FROM python:3.11.3-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requerimientos al contenedor
COPY requirements.txt requirements.txt

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación al contenedor
COPY . .

# Exponer el puerto en el que la aplicación se ejecutará
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["reflex", "run"]