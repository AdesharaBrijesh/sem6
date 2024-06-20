<?php
session_start();
include 'db_connect.php';

if (!isset($_SESSION['admin'])) {
    header('Location: admin_login.php');
    exit;
}

if (isset($_GET['id'])) {
    $id = $_GET['id'];
    $delete_sql = "DELETE FROM students WHERE id='$id'";
    if (mysqli_query($conn, $delete_sql)) {
        $_SESSION['message'] = "Record deleted successfully.";
    } else {
        $_SESSION['message'] = "Error deleting record.";
    }
}

header('Location: admin_dashboard.php');
?>
