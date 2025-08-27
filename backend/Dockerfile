# Dockerfile para Backend Flask

# Imagen base oficial de Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar requirements.txt y luego instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código del backend
COPY . .

# Exponer el puerto en el que Flask corre
EXPOSE 5000

# Comando para correr Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
