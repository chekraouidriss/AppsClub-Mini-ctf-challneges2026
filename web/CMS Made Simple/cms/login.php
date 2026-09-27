<?php
$conn = new mysqli("localhost", "cms_user", "password123", "cms");

$user = $_POST['username'];
$pass = $_POST['password'];

$query = "SELECT * FROM users WHERE username='$user' AND password='$pass'";
$result = $conn->query($query);

if ($result && $result->num_rows > 0) {
    $row = $result->fetch_assoc();
    echo "Welcome " . $row['username'];
}else {
    echo "Invalid login";
}
?>