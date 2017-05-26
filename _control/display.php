<?php 
  $msg = "";
  if (isset($_POST["display"])){
    $msg = $_POST["display"]["msg"];
  }
  $pathFile = "../_model/display.txt";
  $myfile = fopen($pathFile, "w");
  fwrite($myfile, $msg);
  fclose($myfile);
?>