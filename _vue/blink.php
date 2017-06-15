<form id="blink" action="post.php" method="post">
  <div class="checkbox">
    <label><input type="checkbox" value="" id="blink_ck" name="blink_ck">Active</label>
  </div>
  <input type="submit" name="submit" value="Submit" />
</form>

<!-- the result of the search will be rendered inside this div -->
<div id="result_blink"></div>
 
<script>
  // Attach a submit handler to the form
  $( "#blink" ).submit(function( event ) {

    // Stop form from submitting normally
    event.preventDefault();

    // Get some values from elements on the page:
    var $form = $( this ),
      term = $form.find( "input[name='blink_ck']" ).val(),
      url = $form.attr( "action" );

    // Send the data using post
    var param = {}
    if ($('input[name="blink_ck"]:checked').length > 0){
      param = { blink: {ck: term } };
    }
    var posting = $.post( url, param );

    // Put the results in a div
    posting.done(function( data ) {
      var content = $( data ).find( "#content" );
      $( "#result_blink" ).empty().append( content );
    });
  });
</script>