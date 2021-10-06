<?php

function my_count($ka, $veta) {
    echo substr_count($veta, $ka) . "\n";
}

function replace($veta, $input) {
    $ret = $veta;
    foreach ($input as $vow) {
	$ret = str_replace($vow, "*", $ret);
    }

    echo $ret . "\n";
}

function remove($veta, $input) {
    $ret = $veta;
    foreach ($input as $vow) {
	$ret = str_replace($vow, " ", $ret);
    }

    echo $ret . "\n";
}

function reverse($word) {
    $rev = strrev($word);
    for ($i = 0; $i < strlen($word); $i++) {
	echo substr_replace($word, "", strlen($word) - $i) . "      " . substr_replace($rev, "", $i + 1) . "\n";
    }
}

$veta = "Ano je ti tu vyborne";
$input = ["a", "e", "i", "o", "u", "y"];

my_count("e", $veta);
replace($veta, $input);
remove($veta, $input);
reverse("slovo");
?>
