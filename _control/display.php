<?php 
  //$liga = "off";
  if (isset($_POST["display"])){
    if (isset($_POST["display"]["ck"]))
      $liga = "on";
    $msg = $_POST["display"]["msg"];
  }
  $pathFile = "../_model/display.txt";
  $myfile = fopen($pathFile, "w");
  //fwrite($myfile, $liga);
  fwrite($myfile, $msg);
  fclose($myfile);
?>