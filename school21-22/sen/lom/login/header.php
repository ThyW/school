<head>
    <link href="styles.css" rel="stylesheet" type="text">
    <title><?php echo $_SERVER['PHP_SELF'];?></title>
</head>

<header>
    <h1>Moja web app</h1>
    <nav>
	<list>
	    <a href="index.php">Homepage</a>
	    <a href="login.php">Login</a>
	</list>
    </nav>
</header>

<?php
session_start();
?>
