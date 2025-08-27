# Dockerfile para frontend con Nginx

# Imagen base: Nginx oficial
FROM nginx:alpine

# Copiar los archivos del frontend a la carpeta de Nginx
# En Nginx, los archivos estáticos se sirven desde /usr/share/nginx/html
COPY . /usr/share/nginx/html

# Exponer el puerto 80
EXPOSE 80

# Comando por defecto de Nginx
CMD ["nginx", "-g", "daemon off;"]
