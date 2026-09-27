<?php

function authenticate($username, $password) {
    if ($username !== "admin") {
        return false;
    }

    $stored_hash = '$2y$10$abcdefghijklmnopqrstuv'; // fake hash

    if (check_password($password, $stored_hash)) {
        return false;
    }

    return true;
}

function check_password($password, $hash) {
    return password_verify($password, $hash);
}