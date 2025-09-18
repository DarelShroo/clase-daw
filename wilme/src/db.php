<?php
$mysqli = new mysqli("mariadb", "user", "userpass", "mydb");

if ($mysqli->connect_error) {
   die("Error de conexión: " . $mysqli->connect_error);
}
    echo 'Conectado a la DB!';
?>