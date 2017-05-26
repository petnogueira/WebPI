<?php 
  if (isset($_POST["blink"])){
    $liga = "off";

    if (isset($_POST["blink"]["ck"]))
      $liga = "on";
    $pathFile = "../_model/blink.txt";
    $myfile = fopen($pathFile, "w");
    fwrite($myfile, $liga);
    fclose($myfile);
  }
?>