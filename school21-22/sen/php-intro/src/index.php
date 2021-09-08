<html>
 <head>
  <title>1st PHP Page</title>
 </head>
 <body>
<?php 
echo '<h1>Time</h1>';
echo "<strong>current time: " . date(DATE_RFC2822) . "</strong>";

$dni = array("pon", "ut", "str", "st", "pia", "sob", "ned");

if (date("N") >= 6)
    echo "<br>vikend</br>";
else
    echo "<br>nie je vikend</br>";
echo "<br>" . $dni[date("N") - 1] . "</br>";

echo "<table>";

for ($i = 0; $i < 10; $i++) {
    echo "<tr>";
    for ($l = 0; $l < 10; $l++) {
	if ($i == 0 and $l == 0) echo "<td></td>";
	if ($i == 0 and $l != 0) echo "<td>" . $l . "</td>";
	if ($i != 0 and $l != 0) echo "<td></td>";
	if ($i !=0 and $l == 0) echo "<td>" . $i . "</td>";
    }
    echo "</tr>";
}
echo "</table>";
  ?>
 </body>
</html>
