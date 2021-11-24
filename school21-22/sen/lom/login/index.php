<?php
include("header.php");

echo "<div><h1>uvodna stranka</h1></div>\n";

if(isset($_SESSION["message"])) { 
echo $_SESSION["message"];
$_SESSION['message'] = "";
}
?>
