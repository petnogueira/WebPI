<?php 
function include_html_vue($path,$title){
	echo "<div class=\"container\">
		  	<div class=\"panel panel-success\">
			    <div class=\"panel-heading\"><h2>".$title."</h2></div>
			    <div class=\"panel-body\">";
					include $path;
	echo     	"</div>
		    </div>
		</div>";
}
?>

<html>
  <?php include "../inc/header.php"; ?>
  <body>
	<nav class="navbar navbar-inverse">
	  <div class="container-fluid">
	    <div class="navbar-header">
	      <a class="navbar-brand" href="#">WebPI</a>
	    </div>
	    <ul class="nav navbar-nav">
	      <li class="active"><a href="#">Home</a></li>
	      <li><a href="#">About</a></li>
	    </ul>
	  </div>
	</nav>

	<?php include_html_vue("../_vue/blink.php","Blink"); 
		  include_html_vue("../_vue/display.php","Display"); 
	?>

  </body>
</html>