<?php
if (isset($_GET['page'])) {
    include($_GET['page']);
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Login Portal</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Admin Login</h1>
    <form method="POST" action="auth.php">
        <!-- admin panel: /edit.php -->

        <input type="text" name="username" placeholder="Username" required><br>
        <input type="password" name="password" placeholder="Password" required><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>