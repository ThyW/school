<html>
<head></head>
<body>
<p>stuff</p>
<?php
for ($i = 0; $i<10; $i++) {
    if ($i % 2 == 0) {
	echo "<p style = \"color: #0000ff\">" . $i . "</p>";
    } else {
	echo "<p style = \"color: #ff0000\">" . $i . "</p>";
    }
}

for ($i = 0; $i < 10; $i++) {
    echo "<p>" . 2 ** $i . "</p>";
}

$arr = [1, 1];

while (count($arr) < 20) {
    $len = count($arr);
    array_push($arr, $arr[$len - 1] + $arr[$len - 2]); 
}

print_r($arr);

$files = scandir("./pics/");

foreach ($files as $file) {
    if ($file == "." or $file == "..") continue;
    echo "<div><img src=\"pics/". $file . "\"></div>";
}

$cislo = rand(100000000, 999999999);

$cislo = (string) $cislo;
$index = rand(0, 8);
$new = "";

for ($i = 0; $i < 3; $i++) {
    if ($index == 8) {
	$index = 0;
    }
     
    $new = $new . $cislo[$index];

    $index++;
}

$x = str_replace($new, "<strong>" . $new . "</strong>", $cislo);

echo "<p> Vyhralo cislo +421" . $x . "! Gratulujeme!</p>";
?>
</body>
<html>
