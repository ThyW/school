<?php
include("header.php");

// session_destroy(); // opak session start
session_unset(); // nukne vsetko
$_SESSION["message"] = "You are logged off";
header("location: index.php")
?>
