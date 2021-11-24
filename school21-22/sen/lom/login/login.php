<?php
include("header.php");

/* $users = array(
array("user" => "mike", "pass" => "1234"),
array("user" => "anna", "pass" => "5555"),
array("user" => "fredo", "pass" => "fredo"),
); */

if (isset($_POST["submit"])) {
    require("functions.php");
    // TODO password
    $connection = connect("turing.gjh.sk", "kapko.j", "--------", "kapko.j");
    $sql_query = "select * from users where username='" . $_POST['user'] . "';";
    $result = $connection->query($sql_query);

    if ($result->num_rows > 0) {
	$row = $result->fetch_asoc();
	if ($_POST['pass'] == $row['password']) {
	    $_SESSION['user'] = $_POST['user'];
	    $_SESSION['uid'] = $row['uid'];
	    header("location: welcome.php");
	} 
    } else {
	    echo "invalid credentials";
    }

    
    /* $done = false;
    foreach($users as $entry) {
	if ($_POST["user"] == $entry["user"] and $_POST["pass"] == $entry["pass"] ) {
	    $_SESSION["user"] = $entry["user"];
	    header("location: welcome.php");
	    $done = true;
	    break;
	}
    }
    if (!$done) echo "fail"; */
}
?>

<form method="post">
    <p>Username<input type=text name="user"></p>
    <p>Password<input type="password" name="pass"></p>
    <p><input type="submit" name="submit" value="yes"></p>
</form>
