<?php
include("header.php");

$users = array(
array("user" => "mike", "pass" => "1234"),
array("user" => "anna", "pass" => "5555"),
array("user" => "fredo", "pass" => "fredo"),
);

if (isset($_POST["submit"])) {
    $done = false;
    foreach($users as $entry) {
	if ($_POST["user"] == $entry["user"] and $_POST["pass"] == $entry["pass"] ) {
	    header("location: welcome.php");
	    $done = true;
	    break;
	}
    }
    if (!$done) echo "fail";
}
?>

<form method="post">
    <p>Username<input type=text name="user"></p>
    <p>Password<input type="password" name="pass"></p>
    <p><input type="submit" name="submit" value="yes"></p>
</form>
