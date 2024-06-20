<?php
session_start();
include 'db_connect.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $enrollment = $_POST['enrollment'];
    $name = $_POST['name'];
    $branch = $_POST['branch'];
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);

    $photo = $_FILES['photo']['name'];
    $photo_tmp = $_FILES['photo']['tmp_name'];
    $photo_folder = 'uploads/' . $photo;

    if (move_uploaded_file($photo_tmp, $photo_folder)) {
        $sql = "INSERT INTO students (enrollment, name, branch, password, photo) VALUES ('$enrollment', '$name', '$branch', '$password', '$photo_folder')";
        if (mysqli_query($conn, $sql)) {
            $_SESSION['message'] = "Registration successful!";
            header('Location: login.php');
        } else {
            $_SESSION['message'] = "Error: " . mysqli_error($conn);
        }
    } else {
        $_SESSION['message'] = "Failed to upload photo.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Registration</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h2>Student Registration</h2>
        <?php
        if (isset($_SESSION['message'])) {
            echo "<p class='error'>" . $_SESSION['message'] . "</p>";
            unset($_SESSION['message']);
        }
        ?>
        <form action="register.php" method="POST" enctype="multipart/form-data">
            <label>Enrollment: </label>
            <input type="text" name="enrollment" required>
            <label>Name: </label>
            <input type="text" name="name" required>
            <label>Branch: </label>
            <select name="branch" required>
                <option value="IT">IT</option>
                <option value="CE">CE</option>
                <option value="IOT">IOT</option>
                <option value="ME">ME</option>
                <option value="EE">EE</option>
            </select>
            <label>Password: </label>
            <input type="password" name="password" required>
            <label>Photo: </label>
            <input type="file" name="photo" required>
            <input type="submit" value="Register">
        </form>
        <a href="login.php">Already have an account? Login here.</a>
    </div>
</body>
</html>
