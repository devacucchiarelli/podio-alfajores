# Dockerfile para Backend Flask

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer el puerto en el que Flask corre
EXPOSE 5000

# Comando para correr Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
