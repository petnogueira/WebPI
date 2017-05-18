<?php
$pathFile = "../py/teste.txt";
if ($_GET["c"] == "y"){
	echo "Process Started";
	$myfile = fopen($pathFile, "w");
	fwrite($myfile, "on");
	fclose($myfile);
}
if ($_GET["c"] == "n"){
	echo "Process Stoped";
	$myfile = fopen($pathFile, "w");
	fwrite($myfile, "off");
	fclose($myfile);
}

?>