<?php

if ($_GET["c"] == "y"){
	echo "Process Started";
	$myfile = fopen("teste.txt", "w");
	fwrite($myfile, "on");
	fclose($myfile);
}
if ($_GET["c"] == "n"){
	echo "Process Stoped";
	$myfile = fopen("teste.txt", "w");
	fwrite($myfile, "off");
	fclose($myfile);
}

?>