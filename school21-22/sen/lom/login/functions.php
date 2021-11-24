<?php
function connect($server, $user, $password, $db) {
    $connection = new mysqli($server, $user, $password, $db);
    if($connection->connect_error) die("Connection error: " . $connection->connect_error); return null;
    return $connection;
}
?>
