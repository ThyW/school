<?php
include("header.php");

if (isset($_SESSION["user"])) 
{
    echo "<h1>Welcome " . $_SESSION['user'] . "</h1>";
    echo '<a href="logout.php">logout</a>';
}
?>
