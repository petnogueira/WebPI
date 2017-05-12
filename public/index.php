<?php

if ($_GET["c"] == "y"){
	echo "Process Started";
	system("sudo python ../py/blink.py");
}
if ($_GET["c"] == "n"){
	echo "Process Stoped";
	system("sudo pkill -9 'python'");
}

?>