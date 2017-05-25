<div class="container">
  <h2>Help text</h2>
  <p>Use the .help-block class to add a block level help text in forms:</p>
  <form id="display" action="post.php" method="post">
    <div class="checkbox">
      <label><input type="checkbox" value="" name="display[ck]" <?php if ($liga == "on") echo "checked";?>>Active</label>
    </div>
    <div class="form-group">
      <label for="msg">Password:</label>
      <input type="text" class="form-control" id="display_msg" name="display[msg]" placeholder="Enter mesage">
      <span class="help-block">This is some help text that breaks onto a new line and may extend more than one line.</span>
    </div>
    <button type="submit" class="btn btn-default">Submit</button>
  </form>
</div>
