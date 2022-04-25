<?php
require("robo.php");
header("Content-Type: application/json");

if (isset($_POST)) {
    json_encode(array('POST' => $_POST, 'GET' => $_GET ));
    if (!$_POST['key'] == "helloworld")
	echo json_encode(array("error" => "bad"));
	return;
    echo select($_POST['id']);
}
?>
