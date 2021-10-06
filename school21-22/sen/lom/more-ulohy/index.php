<?php 

function spriemeruj() {
    $arr = [];
    for ($i = 0; $i < 10; $i++) {
	array_push($arr, random_int(0, 100));
    }

    $max = 0;
    foreach ($arr as $val) {
	$max = $max +  $val;
    }

    return $max / 10;
}

echo spriemeruj();

$names = array("jano", "jana", "jozo", "david", "fero", "ema", "palo", "adam", "martin", "riso");
function ha($names) {
    $a = [];
    for($i = 0; $i < 10; $i++) {
	$semiarr = [];
	$name = array_rand($names);
	$name = $names[$name];
	
	array_push($semiarr, $name, random_int(100, 200), random_int(0, 99), random_int(0, 1));
	array_push($a, $semiarr);	
    }    

    return $a;
}

print_r(ha($names));

echo "<table>";

foreach (ha($names) as $pacos) {
    echo "<tr>";
    foreach ($pacos as $field) {
	echo "<td>" . $field . "</td>";
    }
    echo "</tr>";
}

echo "</table>";

function fac($n) {
    if ($n == 1) return;
    return $n * fac($n - 1);
}

echo fac(3);
?>
