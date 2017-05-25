
<div class="container">
  <h2>Blink</h2>
  <form id="blink" action="post.php" method="post">
    <p>Blink: </p>
    <div class="checkbox">
      <label><input type="checkbox" value="" name="blink[ck]" <?php if ($liga == "on") echo "checked";?>>Active</label>
    </div>
    <input type="submit" name="submit" value="Search" />
  </form>
</div>