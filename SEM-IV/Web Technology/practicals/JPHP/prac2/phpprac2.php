<?php
$var = "heyy";
$num = 10;
echo $var;
$var="hello";
define('demo', "this is php");
?>
<!DOCTYPE html>
<html>
<head>
	<title>phpprac2</title>
</head>
<body>
<h1><?php echo "Hello php<br>"; ?></h1>
<div><?php
$txt1 = "this is PHP<br>";
$x = 5;
$y = 5;
function display() {
    echo "<br>Statement inside the functions..<br>";
}
echo "<h1>" . $txt1 . "</h1>";
print "5 + 5 = " .($x + $y). "<br>";
echo "<br>";
$fruits = array("apple","mango","watermelon");
var_dump($fruits);
echo "<br>";
display();
echo "<br>";
function displaystr($str) {
    echo "$str <br>";
}

displaystr("function");
displaystr("with parameters");

$str="<h3>Global String</h3>";
function disGlobal()
{
	echo $GLOBALS['str'];
}
disGlobal();
echo $_SERVER['PHP_SELF'];
echo "<br>";
echo $_SERVER['SERVER_NAME'];
echo "<br>";
echo $_SERVER['HTTP_HOST'];
echo "<br>";
echo $_SERVER['HTTP_USER_AGENT'];
echo "<br>";
echo $_SERVER['SCRIPT_NAME'];
?>
</div><br> 
<form method="get" name="f1" action="form.php">
Name: <input type="text" name="name"><br>
E-mail: <input type="text" name="email"><br>
<input type="submit">
</form>
</body>
</html>
