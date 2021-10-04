<html>
<body>
<?php
$dir = './pics/';

$images = scandir($dir);

foreach ($images as &$image) {
    if ($image == '.' || $image == '..') {
	continue;
    }
    echo '<img src="' . $dir . $image . '"/>'; 
};
?>
</body>
</html>
