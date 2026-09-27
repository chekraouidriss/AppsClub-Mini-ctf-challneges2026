<?php
require_once "auth.php";

// <a href="?page=home.php">Home</a>
// <a href="?page=auth.php">Login</a>
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $user = $_POST["username"];
    $pass = $_POST["password"];

    if (authenticate($user, $pass)) {
        echo "Welcome admin!<br>";
        echo "Flag: " . getenv("FLAG");
    } else {
        echo "Invalid credentials";
    }
}
?>