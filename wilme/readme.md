# 🚀 Proyecto PHP + MariaDB con Docker Compose

Este proyecto levanta un entorno completo con **PHP (Apache)** y **MariaDB** usando contenedores Docker.  
Perfecto para desarrollo local sin complicaciones de instalación.

---

## 📂 Estructura del proyecto

```
clase-daw/
│── docker-compose.yml   # Configuración de los servicios
│── src/                 # Código PHP
│   └── index.php
```

> ⚠️ La carpeta `src/` se monta dentro del contenedor de PHP en `/var/www/html`.

---

## 🛠️ Requisitos

- [Docker](https://docs.docker.com/get-docker/)  
- [Docker Compose](https://docs.docker.com/compose/)  

---

## ▶️ Cómo levantar el proyecto

1. Clona este repositorio o descarga los archivos.
2. Sitúate en la carpeta del proyecto:

   ```bash
   cd clase-daw
   ```

3. Levanta los contenedores:

   ```bash
   docker compose up -d --build
   ```

4. Accede a la aplicación en tu navegador:  
   👉 [http://localhost:8080](http://localhost:8080)

---

## 🐘 Servicios

- **PHP (Apache)**  
  - URL: [http://localhost:8080](http://localhost:8080)  
  - Carpeta raíz: `./src`

- **MariaDB**  
  - Host interno: `mariadb`  
  - Puerto expuesto: `3306`  
  - Usuario: `user`  
  - Password: `userpass`  
  - Base de datos: `mydb`

Ejemplo conexión desde PHP:

```php
<?php
$mysqli = new mysqli("mariadb", "user", "userpass", "mydb");

if ($mysqli->connect_error) {
    die("❌ Error de conexión: " . $mysqli->connect_error);
}

echo "✅ Conexión exitosa a MariaDB desde PHP!";
```

---

## 🛑 Cómo detener los contenedores

```bash
docker compose down
```

Si quieres limpiar volúmenes y borrar datos de la BD:

```bash
docker compose down -v
```

---

## 💡 Extras recomendados

Si quieres gestionar MariaDB desde el navegador, puedes añadir **phpMyAdmin** en tu `docker-compose.yml`:

```yaml
phpmyadmin:
  image: phpmyadmin/phpmyadmin
  ports:
    - "8081:80"
  environment:
    PMA_HOST: mariadb
    PMA_USER: user
    PMA_PASSWORD: userpass
  depends_on:
    - mariadb
```

Luego entras en 👉 [http://localhost:808](http://localhost:8081)

---

✨ ¡Listo! Ya tienes tu entorno PHP + MariaDB corriendo con Docker Compose.
