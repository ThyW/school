<?php
function connect($host, $usr, $pass, $db) {
    $mysqli = new mysqli($host, $usr, $pass, $db);
    if ($mysqli->connect_error) {
	die("neni connect");
	return null;
    }

    return $mysqli;
}

function select($id) {
    $err = array('error' => "something was null");
    $con = connect("ha", "ha", "ha", "ha");
    if(!$conn) {
	return json_encode($err);
    }

    $stmt = $con->prepare("SELECT * FROM items WHERE id=?");
    $stmt->bind_param("i", $id);
    $stmt->execute();
    $res = $stmt->get_result();
    $row = $res->fetch_assoc();
    if (!$row) {
	return json_encode($err);
    }

    return json_encode($row);
}
?>
