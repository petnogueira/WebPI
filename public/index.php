
<html>
<?php 
    include "../inc/header.php";

    $pathFile = "../py/teste.txt";
    if (isset($_POST["ck"])){
        $myfile = fopen($pathFile, "w");
        fwrite($myfile, "on");
        fclose($myfile);
    }else{
        $myfile = fopen($pathFile, "w");
        fwrite($myfile, "off");
        fclose($myfile);
    }
?>
<body>
<div class="container">
  <h2>Blink</h2>
  <form id="blink" action="index.php" method="post">
    <p>Blink: </p>
    <div class="checkbox">
      <label><input type="checkbox" value="" name="ck" <?php if (isset($_POST["ck"])) echo "checked";?>>Active</label>
    </div>
    <input type="submit" name="submit" value="Submit" />
  </form>
</div>
</body>
</html>