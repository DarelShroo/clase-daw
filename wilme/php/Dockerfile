FROM php:8.2-apache

# Instalar extensiones necesarias (mysqli, pdo, etc.)
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Copiar el código fuente al contenedor
COPY ./src /var/www/html

# Dar permisos a Apache
RUN chown -R www-data:www-data /var/www/html

EXPOSE 80
