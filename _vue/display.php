<?php 
$msg_checked = "";
if (isset($liga))
  if ($liga == "on") 
    $msg_checked = "checked";
?>
<form id="display" action="post.php" method="post">
  <div class="checkbox disabled">
    <label><input type="checkbox" value="" name="display[ck]" <?php echo $msg_checked;?> disabled>Active</label>
  </div>
  <div class="form-group">
    <label for="msg">Enter your mesage to be display:</label>
    <input type="text" class="form-control" id="display_msg" name="display[msg]" placeholder="Enter mesage">
    <!-- span class="help-block">This is some help text that breaks onto a new line and may extend more than one line.</span -->
  </div>
  <input type="submit" name="submit" value="Submit" />
</form>
<!-- the result of the search will be rendered inside this div -->
<div id="result_display"></div>
 
<script>
  // Attach a submit handler to the form
  $( "#display" ).submit(function( event ) {

    // Stop form from submitting normally
    event.preventDefault();

    // Get some values from elements on the page:
    var $form = $( this ),
      term = $form.find( "input[name='display[msg]']" ).val(),
      url = $form.attr( "action" );

    // Send the data using post
    var param = { display: { msg: term } };

    var posting = $.post( url, param );

    // Put the results in a div
    posting.done(function( data ) {
      var content = $( data ).find( "#content" );
      $( "#result_display" ).empty().append( content );
    });
  });
</script>