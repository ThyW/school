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

for ($row = 0; $num < 10; $row++) {
    echo "<tr>";
    echo "<td></td>";
    for ($data = 1 )
}

  ?>
 </body>
</html>
