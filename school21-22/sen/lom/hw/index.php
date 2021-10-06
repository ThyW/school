<?php

function my_count($ka, $veta) {
    echo substr_count($veta, $ka) . "\n";
}

function replace($veta) {
    $ret = $veta;
    $vowels = ["a", "e", "i", "o", "u", "y"];
    foreach ($vowels as $vow) {
	$ret = str_replace($vow, "*", $ret);
    }

    echo $ret . "\n";
}

function remove($veta) {
    $ret = $veta;
    $vowels = ["a", "e", "i", "o", "u", "y"];
    foreach ($vowels as $vow) {
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

my_count("e", $veta);
replace($veta);
remove($veta);
reverse("slovo");
?>
