<?php
session_start();
include 'db_connect.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $enrollment = $_POST['enrollment'];
    $password = $_POST['password'];

    $sql = "SELECT * FROM students WHERE enrollment='$enrollment'";
    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) == 1) {
        $row = mysqli_fetch_assoc($result);
        if (password_verify($password, $row['password'])) {
            $_SESSION['username'] = $row['name'];
            $_SESSION['enrollment'] = $row['enrollment'];
            header('Location: welcome.php');
        } else {
            $_SESSION['message'] = "Invalid password.";
        }
    } else {
        $_SESSION['message'] = "Invalid enrollment number.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Login</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h2>Student Login</h2>
        <?php
        if (isset($_SESSION['message'])) {
            echo "<p class='error'>" . $_SESSION['message'] . "</p>";
            unset($_SESSION['message']);
        }
        ?>
        <form action="login.php" method="POST">
            <label>Enrollment: </label>
            <input type="text" name="enrollment" required>
            <label>Password: </label>
            <input type="password" name="password" required>
            <input type="submit" value="Login">
        </form>
        <a href="register.php">Don't have an account? Register here.</a>
    </div>
</body>
</html>
